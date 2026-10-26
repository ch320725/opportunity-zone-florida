# OZ parcel pull - v2026-10-26 (adds sale history, just value, expanded corridors)
import json,csv,urllib.request,urllib.parse,datetime,re,sys
oz=json.load(open('oz_geom.geojson'));M={'071':'Lee','021':'Collier','015':'Charlotte'}
COR={'Lee':['41','TAMIAMI','CLEVELAND','COLONIAL','DANIELS','ALICO','THREE OAKS','BAYSHORE'],
'Collier':['41','TAMIAMI','IMMOKALEE','GOLDEN GATE','NAPLES','MAIN ST','NEW MARKET'],
'Charlotte':['41','TAMIAMI','KINGS','MIDWAY','PORT CHARLOTTE','PUNTA GORDA']}
LEE='https://gismapserver.leegov.com/gisserver910/rest/services/DataExplorer/Parcels/MapServer/0/query'
ST='https://services9.arcgis.com/Gh9awoU677aKree0/arcgis/rest/services/Florida_Statewide_Cadastral/FeatureServer/0/query'
COLS=['county','tract_geoid','parcel_id','address','owner','assessed_value','zoning','acreage','last_sale_date','last_sale_price','land_use','corridor_notes','source_url',
      'just_value','prior_sale_date','prior_sale_price','sale_history','owner_mail','lat','lon']
def q(url,where,fields,geom,order,cent=False):
  p=dict(where=where,outFields=fields,returnGeometry='false',f='json',geometry=json.dumps({'rings':geom,'spatialReference':{'wkid':4326}}),
    geometryType='esriGeometryPolygon',inSR=4326,outSR=4326,spatialRel='esriSpatialRelIntersects',orderByFields=order,resultRecordCount=60)
  if cent: p['returnCentroid']='true'
  for i in range(3):
    try:
      r=urllib.request.urlopen(urllib.request.Request(url,data=urllib.parse.urlencode(p).encode()),timeout=90)
      d=json.load(r)
      if 'error' in d: raise Exception(d['error'])
      return d['features']
    except Exception as e:
      err=e
  raise err
def cor(c,a):
  a=(a or '').upper();h=[k for k in COR[c] if (re.search(r'\b(US |HWY |US HIGHWAY )?41\b',a) if k=='41' else k in a)]
  return ('corridor:'+'/'.join(h)) if h else ''
def ld(ms): return datetime.datetime.fromtimestamp(ms/1000,datetime.UTC).date().isoformat() if ms else ''
rows={c:[] for c in M.values()};log=[]
for f in oz['features']:
  g=f['properties']['GEOID10'];c=M[f['properties']['COUNTY']]
  geom=f['geometry']['coordinates'];geom=geom if f['geometry']['type']=='Polygon' else [r for p in geom for r in p]
  try:
    if c=='Lee':
      F=q(LEE,"(DORCODE IN ('00','10','40','70') OR (DORCODE>='11' AND DORCODE<='39') OR (DORCODE>='41' AND DORCODE<='49')) AND GISACRES>=0.25",
        'STRAP,SITEADDR,O_NAME,O_ADDR1,O_CITY,O_STATE,O_ZIP,JUST,ASSESSED,ZONING,GISACRES,S_1DATE,S_1AMOUNT,S_2DATE,S_2AMOUNT,S_3DATE,S_3AMOUNT,S_4DATE,S_4AMOUNT,DORCODE,LANDUSEDES,LATITUDE,LONGITUDE',geom,'GISACRES DESC')
      for ft in F:
        a=ft['attributes']
        hist='; '.join(f"{ld(a[f'S_{i}DATE'])} ${a[f'S_{i}AMOUNT']}" for i in range(1,5) if a.get(f'S_{i}DATE'))
        mail=', '.join(str(x) for x in [a['O_ADDR1'],a['O_CITY'],a['O_STATE'],a['O_ZIP']] if x)
        rows[c].append([c,g,a['STRAP'],a['SITEADDR'],a['O_NAME'],a['ASSESSED'],a['ZONING'],round(a['GISACRES'] or 0,3),ld(a['S_1DATE']),a['S_1AMOUNT'],f"{a['DORCODE']} {a['LANDUSEDES']}",cor(c,a['SITEADDR']),LEE.rsplit('/',1)[0],
          a['JUST'],ld(a['S_2DATE']),a['S_2AMOUNT'],hist,mail,a['LATITUDE'],a['LONGITUDE']])
    else:
      F=q(ST,"(DOR_UC IN ('000','010','040','070') OR (DOR_UC>='011' AND DOR_UC<='039') OR (DOR_UC>='041' AND DOR_UC<='049')) AND LND_SQFOOT>=10890",
        'PARCEL_ID,PHY_ADDR1,PHY_CITY,OWN_NAME,OWN_ADDR1,OWN_CITY,OWN_STATE,OWN_ZIPCD,JV,AV_NSD,LND_SQFOOT,SALE_YR1,SALE_MO1,SALE_PRC1,SALE_YR2,SALE_MO2,SALE_PRC2,DOR_UC,ASMNT_YR',geom,'LND_SQFOOT DESC',cent=True)
      for ft in F:
        a=ft['attributes'];ce=ft.get('centroid') or {}
        sd=lambda n:(f"{a['SALE_YR'+n]}-{int(a['SALE_MO'+n]):02d}" if a['SALE_YR'+n] and a['SALE_MO'+n] else (a['SALE_YR'+n] or ''))
        hist='; '.join(f"{sd(n)} ${a['SALE_PRC'+n]}" for n in '12' if a['SALE_YR'+n])
        mail=', '.join(str(x) for x in [a['OWN_ADDR1'],a['OWN_CITY'],a['OWN_STATE'],a['OWN_ZIPCD']] if x)
        rows[c].append([c,g,a['PARCEL_ID'],f"{a['PHY_ADDR1'] or ''} {a['PHY_CITY'] or ''}".strip(),a['OWN_NAME'],a['AV_NSD'],'',round((a['LND_SQFOOT'] or 0)/43560,3),sd('1'),a['SALE_PRC1'],f"DOR {a['DOR_UC']} (JV {a['JV']}, roll {a['ASMNT_YR']})",cor(c,a['PHY_ADDR1']),ST.rsplit('/',1)[0],
          a['JV'],sd('2'),a['SALE_PRC2'],hist,mail,ce.get('y'),ce.get('x')])
    log.append(f'{c} {g}: {len(F)} rows')
  except Exception as e: log.append(f'{c} {g}: FAIL {e}')
  print(log[-1],flush=True)
for c,r in rows.items():
  with open(f'{c}/{c.lower()}_oz_parcels.csv','w',newline='') as fh:
    w=csv.writer(fh);w.writerow(COLS);w.writerows(r)
  print(c,len(r))
open('pull_log.txt','w').write(f'pull {datetime.datetime.now().isoformat()} (America/New_York)\n'+'\n'.join(log))
