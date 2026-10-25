import pandas as pd,re,json,shutil
BAD=r"COUNTY|CITY OF|STATE OF|SCHOOL|BOARD OF|FDOT|DEPT|DEPARTMENT|TRUSTEES|UNITED STATES|AUTHORITY|DISTRICT|HOMEOWNER|HOA\b|CONDO|ASSOC|PROPERTY OWNERS|COMMON|CHURCH|MINIST|DIOCESE|BAPTIST|METHODIST|LUTHERAN|TEMPLE|CONGREGATION|USA\b"
out={};sl={}
for c in ['Lee','Collier','Charlotte']:
  d=pd.read_csv(f'{c}/{c.lower()}_oz_parcels.csv',dtype={'tract_geoid':str,'parcel_id':str});out[c]=d
  code=d.land_use.str.extract(r'(\d+)')[0].astype(int)
  corr=d.corridor_notes.fillna('').str.len()>0
  own=d.owner.fillna('').str.upper().str.contains(BAD,regex=True)
  vacci=code.isin([10,40]); com=code.between(11,39)|code.between(41,49)
  trailer=code.isin([28])
  keep=(vacci|com|code.isin([70]))&~own
  size=d.acreage.between(0.25,20)|(vacci&(d.acreage>20))
  keep&=size
  keep&=~(trailer&~corr)
  s=d[keep].copy()
  s['priority']=(vacci*3+corr*2+com*1)[keep]
  s['notes']=s.apply(lambda r:('trailer-park tract (corridor)' if re.search(r'\b28\b',str(r.land_use)[:4]) else ''),axis=1)
  s=s.sort_values(['priority','acreage'],ascending=False)
  s.to_csv(f'{c}/{c.lower()}_oz_shortlist.csv',index=False);sl[c]=s;print(c,len(s),'vacant comm/ind:',int(vacci[keep].sum()),'corridor:',int(corr[keep].sum()))
t=json.load(open('oz-tracts.json'));T=pd.DataFrame([(k,g) for k,v in t['counties'].items() for g in v],columns=['county','tract_geoid']);T['source']=t['source']
FS=pd.DataFrame(columns='county,tract_geoid,address,list_price,beds,baths,sqft,lot_size,days_on_market,agent_name,agent_phone,agent_email,source,listing_url,notes'.split(','))
R=pd.DataFrame({'README':open('PROGRESS.md').read().splitlines()+['','Shortlist filter: land use 10/40 vacant comm/ind, 11-39 commercial, 41-49 industrial, 70; drop gov/HOA/church owners; 0.25-20 ac (larger kept only if vacant 10/40); trailer parks (28) only if corridor; priority = 3*vacant + 2*corridor + 1*commercial.','Generated 2026-10-25 America/New_York (EDT, UTC-4).']})
f='oz-scan-2026-10-25.xlsx'
with pd.ExcelWriter(f) as w:
  R.to_excel(w,sheet_name='README',index=False);T.to_excel(w,sheet_name='Tracts',index=False)
  for c in out: out[c].to_excel(w,sheet_name=f'{c}_Parcels',index=False)
  for c in sl: sl[c].to_excel(w,sheet_name=f'{c}_Shortlist',index=False)
  for c in out: FS.to_excel(w,sheet_name=f'{c}_ForSale',index=False)
for c in out: shutil.copy(f,f'{c}/{f}')
