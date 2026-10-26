# Zillow map-bounds scan per OZ tract; keep only listings whose lat/lon falls inside the tract polygon.
import json,re,time,urllib.parse,subprocess,csv,sys
from shapely.geometry import shape,Point
g=json.load(open('oz_geom.geojson'))
UA='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36'
def find(o,k):
    if isinstance(o,dict):
        for kk,v in o.items():
            if kk==k: yield v
            else: yield from find(v,k)
    elif isinstance(o,list):
        for v in o: yield from find(v,k)
out=[];log=[]
from shapely.geometry import box
def boxes(poly,b,depth=0):
    yield b,depth
jobs=[(f['properties']['GEOID10'],shape(f['geometry']),shape(f['geometry']).bounds,0) for f in g['features']]
while jobs:
    geo,poly,(w,s,e,n),depth=jobs.pop(0)
    for page in (1,2,3):
        q={"pagination":{"currentPage":page},"isMapVisible":True,"mapBounds":{"west":w,"east":e,"south":s,"north":n},
           "filterState":{"sort":{"value":"days"}},"isListVisible":True}
        url="https://www.zillow.com/homes/for_sale/?searchQueryState="+urllib.parse.quote(json.dumps(q,separators=(',',':')))
        html=subprocess.run(['curl','-s','-m','40','-A',UA,'-H','Accept-Language: en-US,en;q=0.9',url],capture_output=True,text=True).stdout
        m=re.search(r'<script id="__NEXT_DATA__"[^>]*>(.*?)</script>',html,re.S)
        if not m: log.append(f"{geo} p{page}: no data (len {len(html)})");break
        d=json.loads(m.group(1))
        lr=next(find(d,'listResults'),[]) or []
        tot=next(find(d,'totalResultCount'),None)
        if page==1 and tot and tot>123 and depth<4:
            mx,my=(w+e)/2,(s+n)/2
            for bb in [(w,s,mx,my),(mx,s,e,my),(w,my,mx,n),(mx,my,e,n)]:
                if box(*bb).intersects(poly): jobs.append((geo,poly,bb,depth+1))
            log.append(f"{geo} d{depth}: total {tot} -> split");break
        inn=0
        for x in lr:
            ll=x.get('latLong') or {}
            if not ll.get('latitude'): continue
            if poly.contains(Point(ll['longitude'],ll['latitude'])):
                inn+=1
                hi=x.get('hdpData',{}).get('homeInfo',{})
                out.append(dict(tract=geo,address=x.get('address'),price=x.get('price'),status=x.get('statusText'),
                  beds=x.get('beds'),baths=x.get('baths'),sqft=x.get('area'),lot=x.get('lotAreaString') or hi.get('lotAreaValue'),
                  home_type=hi.get('homeType'),dom=hi.get('daysOnZillow'),broker=x.get('brokerName'),url=x.get('detailUrl'),
                  lat=ll['latitude'],lon=ll['longitude'],zpid=x.get('zpid')))
        log.append(f"{geo} p{page}: total {tot}, page {len(lr)}, in-tract {inn}")
        time.sleep(2.5)
        if len(lr)<41: break
print("\n".join(log))
seen=set();rows=[]
for r in out:
    if r['zpid'] in seen: continue
    seen.add(r['zpid']);rows.append(r)
with open('zillow_oz_2026-10-26.csv','w',newline='') as fh:
    wr=csv.DictWriter(fh,fieldnames=list(rows[0].keys()) if rows else ['tract']);wr.writeheader();wr.writerows(rows)
print(len(rows),'in-tract listings')
