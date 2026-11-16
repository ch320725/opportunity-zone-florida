# 2026-11-16: Zillow-confirmed curated rows updated from this week's in-OZ map scan.
# Commercial-only sources (LoopNet, Crexi) were still blocked; those rows are carried forward as not re-checked.
import copy
from curated_listings_2026_11_02 import L as L0

Z='Zillow map search 2026-11-16 (coords inside OZ polygon)'
U={
 '954 Capetown Ave':dict(status='Active',dom=202,v=Z+'; still $19,900, Coldwell Banker Preferred Properties'),
 '1022 Asther St E':dict(status='Active',dom=202,v=Z+'; still $19,900, Coldwell Banker Preferred Properties'),
 '933 Commodore St':dict(status='Active',dom=202,v=Z+'; still $24,900, Coldwell Banker Preferred Properties'),
 '1048 Redbank Ave':dict(status='Active',dom=195,v=Z+'; still $44,900, Alliance Realty Group'),
 '385 McArthur Blvd':dict(status='Active',dom=202,v=Z+'; still $29,900, Coldwell Banker Preferred Properties'),
 '850 Genoa Ave S':dict(status='Active',dom=188,v=Z+'; still $17,900, Coldwell Banker Preferred Properties'),
 '540 Columbus Blvd S':dict(status='Active',dom=202,v=Z+'; still $19,900, Coldwell Banker Preferred Properties'),
 '3428 Meadow Rd':dict(status='Active',dom=334,agent_name='Key & Legacy Realty LLC (per Zillow)',v=Z+'; still $999,999, Key & Legacy Realty LLC'),
 '3608 Sammy Watkins Ave':dict(status='Active',dom=40,v=Z+'; still $525,000, LSI Companies Inc.'),
 '203 Del Prado Blvd N':dict(status='Active',dom=96,v=Z+'; still $799,000, Properties in Paradise Real Estate, LLC'),
 '2440 Placida Rd':dict(status='Active',dom=529,v=Z+'; Zillow lists as "2440 PLACIDA ROAD LOT 1, ENGLEWOOD, FL 34224", still $625,000'),
 '12691 State Road 31':dict(status='Active',dom=468,agent_name='NRT Commercial LLC (per Zillow)',v=Z+'; still $750,000, NRT Commercial LLC'),
}

L=[]
for r in L0:
    r=copy.deepcopy(r); key=r['address'].split(',')[0]
    u=U.get(key)
    last=str(r.pop('verify_2026_11_02',''))[:200]
    if u:
        if 'price' in u: r['list_price']=u['price']
        for k in ('status','lot_size','agent_name','agent_phone','agent_email'):
            if k in u: r[k]=u[k]
        if 'dom' in u: r['days_on_market']=u['dom']
        if u.get('note'): r['notes']=('; '.join(x for x in [u.get('note',''),str(r.get('notes') or '')] if x))
        r['verify_2026_11_16']=u.get('v','')
    else:
        r['verify_2026_11_16']='not re-checked 2026-11-16; last verified: '+last
        sl=r['status'].lower()
        if not any(x in sl for x in ('sold','removed')) and 'not re-checked 2026-11-16' not in sl:
            r['status']=r['status']+' (not re-checked 2026-11-16)'
    L.append(r)
