import json,csv,urllib.request,urllib.parse,datetime,re
oz=json.load(open('oz_geom.geojson'));M={'071':'Lee','021':'Collier','015':'Charlotte'}
COR={'Lee':['41','TAMIAMI','CLEVELAND','COLONIAL','DANIELS','ALICO','THREE OAKS','BAYSHORE'],
'Collier':['41','TAMIAMI','IMMOKALEE','GOLDEN GATE','MAIN ST','NEW MARKET'],
'Charlotte':['41','TAMIAMI','KINGS','MIDWAY']}
LEE='https://gismapserver.leegov.com/gisserver910/rest/services/DataExplorer/Parcels/MapServer/0/query'
ST='https://services9.arcgis.com/Gh9awoU677aKree0/arcgis/rest/services/Florida_Statewide_Cadastral/FeatureServer/0/query'
COLS=['county','tract_geoid','parcel_id','address','owner','assessed_value','zoning','acreage','last_sale_date','last_sale_price','land_use','corridor_notes','source_url']
def q(url,where,fields,geom,order):
  p=dict(where=where,outFields=fields,returnGeometry='false',f='json',geometry=json.dumps({'rings':geom,'spatialReference':{'wkid':4326}}),
    geometryType='esriGeometryPolygon',inSR=4326,spatialRel='esriSpatialRelIntersects',orderByFields=order,resultRecordCount=60)
  r=urllib.request.urlopen(urllib.request.Request(url,data=urllib.parse.urlencode(p).encode()),timeout=60)
  d=json.load(r)
  if 'error' in d: raise Exception(d['error'])
  return [f['attributes'] for f in d['features']]
def cor(c,a):
  a=(a or '').upper();h=[k for k in COR[c] if (re.search(r'\b(US |HWY |US HIGHWAY )?41\b',a) if k=='41' else k in a)]
  return ('corridor:'+'/'.join(h)) if h else ''
rows={c:[] for c in M.values()};log=[]
for f in oz['features']:
  g=f['properties']['GEOID10'];c=M[f['properties']['COUNTY']]
  geom=f['geometry']['coordinates'];geom=geom if f['geometry']['type']=='Polygon' else [r for p in geom for r in p]
  try:
    if c=='Lee':
      A=q(LEE,"(DORCODE IN ('00','10','40','70') OR (DORCODE>='11' AND DORCODE<='39') OR (DORCODE>='41' AND DORCODE<='49')) AND GISACRES>=0.25",
        'STRAP,SITEADDR,O_NAME,JUST,ASSESSED,ZONING,GISACRES,S_1DATE,S_1AMOUNT,DORCODE,LANDUSEDES',geom,'GISACRES DESC')
      for a in A:
        sd=datetime.datetime.utcfromtimestamp(a['S_1DATE']/1000).date().isoformat() if a['S_1DATE'] else ''
        rows[c].append([c,g,a['STRAP'],a['SITEADDR'],a['O_NAME'],a['ASSESSED'],a['ZONING'],round(a['GISACRES'] or 0,3),sd,a['S_1AMOUNT'],f"{a['DORCODE']} {a['LANDUSEDES']}",cor(c,a['SITEADDR']),LEE.rsplit('/',1)[0]])
    else:
      A=q(ST,"(DOR_UC IN ('000','010','040','070') OR (DOR_UC>='011' AND DOR_UC<='039') OR (DOR_UC>='041' AND DOR_UC<='049')) AND LND_SQFOOT>=10890",
        'PARCEL_ID,PHY_ADDR1,PHY_CITY,OWN_NAME,JV,AV_NSD,LND_SQFOOT,SALE_YR1,SALE_MO1,SALE_PRC1,DOR_UC,ASMNT_YR',geom,'LND_SQFOOT DESC')
      for a in A:
        sd=f"{a['SALE_YR1']}-{int(a['SALE_MO1']):02d}" if a['SALE_YR1'] and a['SALE_MO1'] else (a['SALE_YR1'] or '')
        rows[c].append([c,g,a['PARCEL_ID'],f"{a['PHY_ADDR1'] or ''} {a['PHY_CITY'] or ''}".strip(),a['OWN_NAME'],a['AV_NSD'],'',round((a['LND_SQFOOT'] or 0)/43560,3),sd,a['SALE_PRC1'],f"DOR {a['DOR_UC']} (JV {a['JV']}, roll {a['ASMNT_YR']})",cor(c,a['PHY_ADDR1']),ST.rsplit('/',1)[0]])
    log.append(f'{c} {g}: {len(A)} rows')
  except Exception as e: log.append(f'{c} {g}: FAIL {e}')
  print(log[-1],flush=True)
for c,r in rows.items():
  with open(f'{c}/{c.lower()}_oz_parcels.csv','w',newline='') as fh:
    w=csv.writer(fh);w.writerow(COLS);w.writerows(r)
  print(c,len(r))
open('pull_log.txt','w').write('\n'.join(log));print('\n'.join(log))
