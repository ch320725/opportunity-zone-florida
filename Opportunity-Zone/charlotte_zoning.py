import pandas as pd,urllib.request,urllib.parse,json
from concurrent.futures import ThreadPoolExecutor
B='https://agis3.charlottecountyfl.gov/arcgis/rest/services/Essentials/CCGISLayers/MapServer/'
def z(lat,lon):
  for lyr in ('43','29'):
    p=dict(geometry=f'{lon},{lat}',geometryType='esriGeometryPoint',inSR=4326,spatialRel='esriSpatialRelIntersects',outFields='*',returnGeometry='false',f='json')
    try:
      d=json.load(urllib.request.urlopen(urllib.request.Request(B+lyr+'/query?'+urllib.parse.urlencode(p),headers={'User-Agent':'Mozilla/5.0'}),timeout=60))
      if d.get('features'):
        a=d['features'][0]['attributes'];v=a.get('ZONE_') or a.get('ZONE') or a.get('ZONING') or next((str(x) for k,x in a.items() if 'ZON' in k.upper() and x),None)
        if v: return v+(' (Punta Gorda)' if lyr=='29' else '')
    except Exception as e: return f'ERR {e}'
  return ''
f='Charlotte/charlotte_oz_parcels.csv';d=pd.read_csv(f,dtype={'tract_geoid':str,'parcel_id':str})
with ThreadPoolExecutor(8) as ex: d['zoning']=list(ex.map(z,d.lat,d.lon))
d.to_csv(f,index=False);print(d.zoning.value_counts().head(20));print((d.zoning=='').sum(),'blank')
