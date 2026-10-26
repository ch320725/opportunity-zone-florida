import json,urllib.request,urllib.parse,functools
from shapely.geometry import shape,Point
from shapely.ops import nearest_points
oz=json.load(open('/workspace/Opportunity-Zone/oz_geom.geojson'))
P=[(f['properties']['GEOID10'],shape(f['geometry'])) for f in oz['features']]
@functools.lru_cache(None)
def geocode(addr):
  u='https://geocoding.geo.census.gov/geocoder/locations/onelineaddress?'+urllib.parse.urlencode(dict(address=addr,benchmark='Public_AR_Current',format='json'))
  try:
    m=json.load(urllib.request.urlopen(u,timeout=40))['result']['addressMatches']
    if m: return m[0]['coordinates']['y'],m[0]['coordinates']['x'],m[0]['matchedAddress']
  except Exception as e: return None
  return None
def tract(lat,lon):
  p=Point(lon,lat)
  for g,s in P:
    if s.contains(p): return g,0.0
  d=min((s.distance(p),g) for g,s in P)
  return None,(d[1],round(d[0]*105,2))  # approx km
def check(addr):
  g=geocode(addr)
  if not g: return dict(geocode='no match',oz_tract='',oz_status='unverified (geocode failed)')
  lat,lon,m=g;t,d=tract(lat,lon)
  if t: return dict(geocode=m,lat=lat,lon=lon,oz_tract=t,oz_status='IN OZ (geocoded)')
  return dict(geocode=m,lat=lat,lon=lon,oz_tract='',oz_status=f'NOT in OZ (nearest {d[0]} ~{d[1]} km)')
LEEQ='https://gismapserver.leegov.com/gisserver910/rest/services/DataExplorer/Parcels/MapServer/0/query'
STQ='https://services9.arcgis.com/Gh9awoU677aKree0/arcgis/rest/services/Florida_Statewide_Cadastral/FeatureServer/0/query'
def _get(u,p):
  return json.load(urllib.request.urlopen(urllib.request.Request(u+'?'+urllib.parse.urlencode(p),headers={'User-Agent':'Mozilla/5.0'}),timeout=60))
def parcel_pt(county,where):
  if county=='Lee':
    d=_get(LEEQ,dict(where=where,outFields='STRAP,SITEADDR,LATITUDE,LONGITUDE,O_NAME',returnGeometry='false',f='json'))
    F=d.get('features',[])
    return [(f['attributes']['LATITUDE'],f['attributes']['LONGITUDE'],f['attributes']['STRAP'],f['attributes']['SITEADDR'],f['attributes']['O_NAME']) for f in F]
  d=_get(STQ,dict(where=where,outFields='PARCEL_ID,PHY_ADDR1,OWN_NAME',returnGeometry='false',returnCentroid='true',outSR=4326,f='json'))
  return [(f['centroid']['y'],f['centroid']['x'],f['attributes']['PARCEL_ID'],f['attributes']['PHY_ADDR1'],f['attributes']['OWN_NAME']) for f in d.get('features',[])]
def check_parcel(county,where):
  r=parcel_pt(county,where)
  if not r: return dict(oz_status='unverified (parcel not found)')
  lat,lon,pid,ad,own=r[0];t,d=tract(lat,lon)
  base=dict(geocode=f'parcel {pid} {ad}',lat=lat,lon=lon,owner=own)
  if t: return dict(base,oz_tract=t,oz_status='IN OZ (parcel)')
  return dict(base,oz_tract='',oz_status=f'NOT in OZ (nearest {d[0]} ~{d[1]} km)')
