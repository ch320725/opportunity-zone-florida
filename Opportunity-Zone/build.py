# Build 2026-10-26 weekly outputs: for_sale CSVs, WoW diff, xlsx, wow md.
import pandas as pd, json, re, os, shutil, datetime as dt
from curated_listings import L
D='2026-10-26'; B='2026-10-25'
C={'Lee':'lee','Collier':'collier','Charlotte':'charlotte'}
tr=json.load(open('oz-tracts.json'))['counties']
cty_of={g:c for c,gs in tr.items() for g in gs}
def norm(a):
    a=str(a).upper().split(',')[0]
    a=re.sub(r'\b(UNIT|APT|#)\s*\S+','',a)
    a=a.replace('TRAIL','TRL').replace('STREET','ST').replace('AVENUE','AVE').replace('BOULEVARD','BLVD').replace('ROAD','RD').replace('PARKWAY','PKWY').replace('PKY','PKWY').replace('DRIVE','DR')
    a=re.sub(r'\bDOCTOR\b','DR',a); a=re.sub(r'MARTIN LUTHER KING( JR)?','MLK',a)
    return re.sub(r'[^A-Z0-9]','',a)
def money(s):
    s=str(s); m=re.sub(r'[^\d.]','',s)
    return float(m) if m else None
COLS=['county','oz_tract','oz_status','status','address','list_price','beds','baths','sqft','lot_size','days_on_market','agent_name','agent_phone','agent_email','source','listing_url','verified_date','verify_method','notes']
cur=pd.DataFrame(L); cur['verified_date']=D
cur['verify_method']=cur.oz_status.map(lambda s:'county parcel coords + OZ polygon' if 'parcel' in s else ('Census geocode + OZ polygon' if s.startswith(('IN','NOT')) else ''))
z=pd.read_csv(f'zillow_oz_{D}.csv',dtype={'tract':str})
z['county']=z.tract.map(cty_of)
z=z[z.price.map(lambda p:(money(p) or 0)>0)]   # drop $0 auction placeholders
zz=pd.DataFrame(dict(county=z.county,oz_tract=z.tract,oz_status='IN OZ (Zillow coords)',status=z.status,address=z.address,
   list_price=z.price.map(money),beds=z.beds,baths=z.baths,sqft=z.sqft,lot_size=z.lot,days_on_market=z.dom,
   agent_name=z.broker,agent_phone='',agent_email='',source='Zillow ('+z.home_type.fillna('')+')',listing_url=z.url,
   verified_date=D,verify_method='Zillow lat/lon + OZ polygon',notes=''))
cur['k']=cur.address.map(norm); zz['k']=zz.address.map(norm)
# enrich curated rows with Zillow URL/DOM where duplicate, then drop dup from zillow set
for i,r in cur.iterrows():
    m=zz[zz.k==r.k]
    if len(m):
        cur.at[i,'notes']=(str(r.notes)+f"; also on Zillow {m.iloc[0].listing_url} (Zillow DOM {m.iloc[0].days_on_market})").strip('; ')
zz=zz[~zz.k.isin(cur.k)]
allfs=pd.concat([cur,zz],ignore_index=True)
def bucket(r):
    s=str(r.status).lower(); o=str(r.oz_status)
    if o.startswith('NOT'): return 'near-OZ reference (not in OZ)'
    if 'sold' in s or 'removed' in s: return 'removed/sold'
    if 'unverified' in s or 'not re-checked' in s or 'confirm' in s or 'stale' in s or 'lease' in s: return 'in OZ - status unverified'
    if 'pending' in s: return 'in OZ - pending'
    return 'in OZ - active'
allfs['bucket']=allfs.apply(bucket,axis=1)
order={'in OZ - active':0,'in OZ - pending':1,'in OZ - status unverified':2,'removed/sold':3,'near-OZ reference (not in OZ)':4}
allfs['_o']=allfs.bucket.map(order)
allfs['_src']=allfs.source.str.startswith('Zillow').astype(int)
FS={}
for c,lc in C.items():
    d=allfs[allfs.county==c].sort_values(['_o','_src','list_price'],ascending=[True,True,False])
    d=d[['bucket']+COLS]; FS[c]=d
    d.to_csv(f'{c}/{lc}_for_sale.csv',index=False)
# ---------- parcels / shortlist ----------
P={c:pd.read_csv(f'{c}/{lc}_oz_parcels.csv',dtype={'tract_geoid':str,'parcel_id':str}) for c,lc in C.items()}
S={c:pd.read_csv(f'{c}/{lc}_oz_shortlist.csv',dtype={'tract_geoid':str,'parcel_id':str}) for c,lc in C.items()}
RAW={c:(len(P[c]),len(S[c])) for c in C}
# FDOR layer returns duplicate records for some multipart parcels -> keep one row per parcel_id+tract
for c,lc in C.items():
    P[c]=P[c].drop_duplicates(['tract_geoid','parcel_id']); S[c]=S[c].drop_duplicates(['tract_geoid','parcel_id'])
    P[c].to_csv(f'{c}/{lc}_oz_parcels.csv',index=False)
# flag shortlisted parcels that are currently listed
for c in C:
    act=allfs[(allfs.county==c)&allfs.bucket.str.startswith('in OZ')]
    keys={k:v for k,v in zip(act.k,act.listing_url.fillna('')+' $'+act.list_price.astype(str)) if re.match(r'\d',k)}
    S[c]['listed_now']=S[c].address.map(lambda a:keys.get(norm(a),''))
    S[c].to_csv(f'{c}/{C[c]}_oz_shortlist.csv',index=False)
# ---------- WoW ----------
W=[]
def w(c,cat,key,field,old,new,note=''): W.append(dict(county=c,category=cat,key=key,field=field,old=old,new=new,note=note))
for c,lc in C.items():
    o=pd.read_csv(f'{c}/history/{B}/{lc}_oz_parcels.csv',dtype={'tract_geoid':str,'parcel_id':str}).drop_duplicates('parcel_id').set_index('parcel_id')
    n=P[c].drop_duplicates('parcel_id').set_index('parcel_id')
    for pid in n.index.difference(o.index): w(c,'parcel added',pid,'',None,n.at[pid,'address'])
    for pid in o.index.difference(n.index): w(c,'parcel dropped',pid,'',o.at[pid,'address'],None)
    zfill=0
    for pid in n.index.intersection(o.index):
        for f in ['owner','assessed_value','acreage','last_sale_date','last_sale_price','zoning']:
            a,b=o.at[pid,f],n.at[pid,f]
            if pd.isna(a) and pd.isna(b): continue
            if f in('assessed_value','acreage','last_sale_price'):
                try:
                    if abs(float(a)-float(b))<1e-6: continue
                except: pass
            elif str(a)==str(b): continue
            if f=='zoning' and pd.isna(a): zfill+=1; continue
            w(c,'parcel change',pid,f,a,b,n.at[pid,'address'])
    if zfill: w(c,'data enrichment','(all)','zoning',f'blank on {zfill} parcels',f'filled from Charlotte County zoning layer','not a real zoning change')
    os_=pd.read_csv(f'{c}/history/{B}/{lc}_oz_shortlist.csv',dtype={'parcel_id':str})
    a_,b_=set(os_.parcel_id),set(S[c].parcel_id)
    w(c,'shortlist','(summary)','unique parcels',len(a_),len(b_),f'+{len(b_-a_)} / -{len(a_-b_)}; rows {len(os_)} -> {len(S[c])} after de-duplicating FDOR duplicate records')
    w(c,'parcels','(summary)','rows',RAW[c][0],len(P[c]),f'unique parcel_id+tract; {len(o)} unique in baseline')
    # listings
    ol=pd.read_csv(f'{c}/history/{B}/{lc}_for_sale.csv'); ol['k']=ol.address.map(norm)
    cc=cur[cur.county==c]
    for _,r in ol.iterrows():
        m=cc[cc.k==r.k]
        if not len(m): w(c,'listing removed',r.address,'',r.list_price,None,'not found'); continue
        m=m.iloc[0]
        if pd.notna(r.list_price) and money(m.list_price) and abs(float(r.list_price)-money(m.list_price))>1:
            w(c,'listing price',r.address,'list_price',r.list_price,m.list_price,m.notes)
        if not str(m.status).startswith('Active'): w(c,'listing status',r.address,'status','listed',m.status,'')
        w(c,'listing OZ check',r.address,'oz_status',r.tract_geoid_or_area,f"{m.oz_status} {m.oz_tract}",'')
        if pd.notna(r.days_on_market) and str(m.days_on_market) not in('','nan'):
            w(c,'listing DOM',r.address,'days_on_market',r.days_on_market,m.days_on_market,'')
    for _,m in cc[~cc.k.isin(ol.k)].iterrows():
        w(c,'listing new to tracker',m.address,'list_price',None,m.list_price,f"{m.oz_status} {m.oz_tract}; {m.status}")
    zc=zz[zz.county==c]
    zn=zc[pd.to_numeric(zc.days_on_market,errors='coerce')<=7]
    w(c,'Zillow coverage (new source)','(summary)','in-OZ Zillow listings',None,len(zc),f'{len(zn)} with Zillow DOM<=7 (listed this week)')
    for _,m in zn.iterrows(): w(c,'Zillow new this week (DOM<=7)',m.address,'list_price',None,m.list_price,f"{m.oz_tract} {m.source} {m.listing_url}")
WW=pd.DataFrame(W)
# ---------- xlsx ----------
readme=[['Southwest Florida Opportunity Zone scan',D],['Counties','Lee (15 tracts), Collier (5), Charlotte (3) - 2010-tract QOZ designations (OZ 1.0, in effect through 2028-12-31)'],
 ['Parcels','Lee: Lee County Parcels MapServer; Collier & Charlotte: FDOR Florida Statewide Cadastral. Spatial intersect with each OZ tract; DOR use filter, >=0.25 ac, top 60/tract by acreage'],
 ['Charlotte zoning','NEW: filled via point-in-polygon on Charlotte County agis3 CCGISLayers layers 43/29'],
 ['Collier zoning','GAP: no public Collier zoning REST endpoint found'],
 ['Shortlist','Rules unchanged from 2026-10-25 (vacant comm/ind, corridor, size, priority score). listed_now = currently listed in-OZ listing matched by address'],
 ['ForSale','bucket: in OZ - active / pending / status unverified / removed-sold / near-OZ reference. OZ check = point-in-polygon of listing coords (Census geocoder, county parcel coords, or Zillow lat/lon) vs OZ tract polygons'],
 ['ForSale sources','Curated: Coldwell Banker, realty.com, Crexi, TotalCommercial, RI Marketplace, CommercialSearch, Suncoast, raveis, keysofsarasota, Trinity CRE. Systematic: Zillow map-bounds per tract (quad-split)'],
 ['Gaps','LoopNet 403 (status of LoopNet-only listings unverified); Realtor.com 429; Douglas Elliman captcha; theguillettegroup 429; realmo curl 403; Zillow shows brokerage only (no agent phone/email) and excludes most commercial-only listings'],
 ['WoW baseline',f'{B} snapshots in <County>/history/{B}/']]
with pd.ExcelWriter(f'oz-scan-{D}.xlsx',engine='openpyxl') as x:
    pd.DataFrame(readme,columns=['item','detail']).to_excel(x,sheet_name='README',index=False)
    pd.DataFrame([(c,g,len(P[c][P[c].tract_geoid==g]),len(S[c][S[c].tract_geoid==g]),
        int(((allfs.county==c)&(allfs.oz_tract==g)&(allfs.bucket=='in OZ - active')).sum())) for c,gs in tr.items() for g in gs],
        columns=['county','tract_geoid','parcels','shortlist','active_listings']).to_excel(x,sheet_name='Tracts',index=False)
    for c in C: P[c].to_excel(x,sheet_name=f'{c}_Parcels',index=False)
    for c in C: S[c].to_excel(x,sheet_name=f'{c}_Shortlist',index=False)
    for c in C: FS[c].to_excel(x,sheet_name=f'{c}_ForSale',index=False)
    WW.to_excel(x,sheet_name='WoW_Changes',index=False)
    for ws in x.book.worksheets:
        ws.freeze_panes='A2'
        for col in ws.columns:
            ws.column_dimensions[col[0].column_letter].width=min(60,max(10,max(len(str(c.value or '')) for c in col[:200])+2))
for c in C:
    shutil.copy(f'oz-scan-{D}.xlsx',f'{c}/oz-scan-{D}.xlsx')
    os.makedirs(f'{c}/weekly/{D}',exist_ok=True)
    for f in [f'{C[c]}_oz_parcels.csv',f'{C[c]}_oz_shortlist.csv',f'{C[c]}_for_sale.csv',f'oz-scan-{D}.xlsx']: shutil.copy(f'{c}/{f}',f'{c}/weekly/{D}/{f}')
WW.to_csv(f'wow-{D}.csv',index=False)
summ={c:dict(tracts=len(tr[c]),parcels=len(P[c]),shortlist=len(S[c]),**FS[c].bucket.value_counts().to_dict(),
     zillow=int((FS[c].source.str.startswith('Zillow')&FS[c].bucket.eq('in OZ - active')).sum())) for c in C}
json.dump(summ,open('summary.json','w'),indent=1,default=str); print(json.dumps(summ,indent=1,default=str))
print(WW.category.value_counts())
