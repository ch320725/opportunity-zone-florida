# Hand-verified listing records for the 2026-11-02 scan (sources fetched/searched 2026-11-02, America/New_York).
# Base records = 2026-10-26 file; U applies only changes confirmed on 2026-11-02. Rows not in U keep last week's values and are
# marked "not re-checked 2026-11-02" when their status was not confirmed this week.
from curated_listings_2026_10_26 import L as L0
import copy
Z='Zillow detail page fetched 2026-11-02 (lat/lon checked vs OZ polygon)'
U={
 '954 Capetown Ave':dict(status='Active',dom=188,lot_size='0.25 ac',agent_name='Fred Elliott (Coldwell Banker Preferred)',agent_phone='239-357-7877',v=Z+'; MLS 2026019275'),
 '1022 Asther St E':dict(status='Active',dom=188,agent_phone='239-357-7877',v=Z),
 '933 Commodore St':dict(status='Active',dom=188,agent_name='Fred Elliott (Coldwell Banker Preferred)',agent_phone='239-357-7877',v=Z),
 '1048 Redbank Ave':dict(status='Active',dom=181,agent_phone='239-281-3497',v=Z),
 '385 McArthur Blvd':dict(status='Active',dom=188,agent_phone='239-357-7877 / office 239-369-6161',v=Z),
 '850 Genoa Ave S':dict(status='Active',dom=174,agent_phone='239-357-7877 / office 239-369-6161',v=Z),
 '540 Columbus Blvd S':dict(status='Active',dom=188,agent_phone='239-357-7877 / office 239-369-6161',v=Z),
 '3428 Meadow Rd':dict(status='Active',dom=320,agent_name='Molly Lira (per Zillow)',agent_phone='239-398-5923',v=Z+'; Zillow now shows listing agent Molly Lira'),
 '3608 Sammy Watkins Ave':dict(status='Active',dom=26,agent_phone='563-505-2197 (Alec Burke, per Zillow)',v=Z+'; Coldwell Banker page also Active $525,000'),
 '3696 Dr Martin Luther King Jr Blvd':dict(status='Active',dom=40,v='TotalCommercial (updated 2026-10-30) + Crexi search result (40 DOM); Crexi page itself 403'),
 '203 Del Prado Blvd N':dict(status='Active',dom=82,agent_name='Joella Consolazio (Properties in Paradise Real Estate)',agent_phone='239-848-5136',v=Z),
 '3171 Dr Martin Luther King Jr Blvd':dict(status='Status unverified (LoopNet blocked; not re-checked 2026-11-02)',v='LoopNet 403; search index still shows $850,000'),
 '1407 Lincoln Ave':dict(status='Status unverified (LoopNet blocked; not re-checked 2026-11-02)',v='LoopNet 403; Zillow shows parcel off-market (commercial land is often not on Zillow)'),
 '4901 Buckingham Rd':dict(status='Active',dom=28,agent_name='Kelly Barnes',agent_phone='239-823-6849',v=Z),
 'W Main St & N 11th St':dict(status='Active',v='RI Marketplace page fetched 2026-11-02: For Sale, $5,500,000'),
 '602 W Main St':dict(status='Status unverified (Trinity brochure not reachable 2026-11-02)',v='trinitycre.com fetch failed; not on MLS (Edina shows off-market public record)'),
 '1312 15th St N':dict(status='Status unverified (LoopNet blocked; not re-checked 2026-11-02)',v='LoopNet 403; search snippet says no longer advertised on LoopNet (last updated 2024-07-23)'),
 'State Road 29':dict(status='Status unverified (LoopNet blocked; not re-checked 2026-11-02)',v='LoopNet 403'),
 '10001 Tamiami Trl E':dict(price=5300000,status='Active for sale per Crexi search result (Crexi page 403); also for lease',dom=393,agent_name='Gary Barlow; Brock Rasmussen, SIOR (Lee & Associates Naples)',
     v='Crexi search result 2026-11-02: $5,300,000, 393 DOM, updated ~72 days ago',note='BASELINE CORRECTION: Crexi sale price $5.3M was set ~72 days ago; 10-26 row carried unverified $6.5M (LoopNet)'),
 '3933 Tollhouse Dr':dict(status='Active',v='search results 2026-11-02 (realmo/raveis MLS 221016013) still active $9,606,022; realmo page 403, DOM not re-checked',dom=''),
 '3893 Mannix Dr #529':dict(price=410000,status='SOLD 2026-08-31 ($410,000)',v='Zillow RECENTLY_SOLD $410,000 + MLS 226023144 search result: sold 2026-08-31',note='Sold before last week; baseline "likely removed" now confirmed sold'),
 '3092 Tamiami Trl':dict(status='Removed (LoopNet: no longer advertised)',v='LoopNet page (via search index 2026-11-02): "no longer advertised"; Zillow off-market; owner SUNSHINE RE HOLDINGS LLC (last sale 2020-09-01 $750,000)'),
 '2901 Placida Rd':dict(status='Active',dom=373,agent_name='G. River West (MSC Commercial); MLS courtesy Bright Realty',agent_phone='863-202-0439 / Bright Realty 941-552-6036',agent_email='RiverWest@MSCCommercial.com',
     v='raveis page fetched 2026-11-02: Active $999,999, DOM 373 (MLS A4665839); RI Marketplace/CommercialSearch $999,999'),
 '2931 Placida Rd':dict(status='Active',dom=407,v='keysofsarasota page fetched 2026-11-02: For sale $2,500,000, 407 days listed'),
 '2900 Placida Rd':dict(status='Pending',dom=17,agent_name='Wagner Realty (MLS A4699827)',v='raveis page fetched 2026-11-02: Pending $1,100,000'),
 '3060 Placida Rd':dict(status='Active',agent_name='Lasbury-Tracy Realty Inc. (MLS D6144764)',v='keysofsarasota similar-listings 2026-11-02: For sale $1,950,000, 3 ac, MLS D6144764'),
 '2440 Placida Rd':dict(status='Active',agent_name='Michael Saunders & Co. - Boca (MLS D6142606); also G. River West (MSC Commercial)',
     v='Coldwell Banker page fetched 2026-11-02: Active $625,000 (reduced from $675,000 on 2025-12-22), MLS D6142606'),
 '12691 State Road 31':dict(status='Active',dom=454,agent_name='Fred Kermani (per Zillow)',agent_phone='239-293-3007',v=Z+' (Zillow DOM 454; MLS DOM 651 last week)'),
 '21202-21234 Olean Blvd Unit 2S':dict(v='search 2026-11-02: Compass still shows active $337,000 (last updated 2024-09-13) - stale risk'),
 '4732 Tamiami Trl':dict(status='Active',v='search 2026-11-02: MLS F10536127 active $2,150,000 (Elliman page blocked)'),
 '16070 Tamiami Trail':dict(status='Active',v='search 2026-11-02: MLS 226028828 active $1,890,000 (Suncoast page 403)'),
 '10000 Tamiami Trail':dict(status='Active',dom=179,agent_name='Jennifer Williams Garcia (per Zillow)',agent_phone='941-763-1963',v=Z),
 '490 Tamiami Trail':dict(status='Active',dom=167,agent_name='J. Lyn Bevis (per Zillow)',agent_phone='941-380-6677',v='Coldwell Banker + '+Z),
 '1900 Tamiami Trail #C-D':dict(status='Active',v='Coldwell Banker page fetched 2026-11-02: Active $1,800,000 (MLS 2026028797)'),
}
L=[]
for r in L0:
    r=copy.deepcopy(r); key=r['address'].split(',')[0]
    u=U.get(key)
    if u:
        if 'price' in u: r['list_price']=u['price']
        for k in ('status','lot_size','agent_name','agent_phone','agent_email'):
            if k in u: r[k]=u[k]
        if 'dom' in u: r['days_on_market']=u['dom']
        r['notes']=('; '.join(x for x in [u.get('note',''),str(r['notes'])] if x))
        r['verify_2026_11_02']=u.get('v','')
    else:
        r['verify_2026_11_02']='not re-checked 2026-11-02'
        if r['status'].startswith('Not re-checked') or 'LoopNet' in r['source']:
            r['status']=r['status'] if 'not re-checked' in r['status'].lower() else r['status']+' (not re-checked 2026-11-02)'
    L.append(r)
