# Fetch a Zillow property page (by address or URL) and return the main property's status/price/DOM/agent.
import re,json,subprocess,urllib.parse
UA='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36'
def find(o,k):
    if isinstance(o,dict):
        for kk,v in o.items():
            if kk==k: yield v
            yield from find(v,k)
    elif isinstance(o,list):
        for v in o: yield from find(v,k)
def fetch(q):
    url=q if q.startswith('http') else 'https://www.zillow.com/homes/'+urllib.parse.quote(q.replace(' ','-'))+'_rb/'
    r=subprocess.run(['curl','-s','-L','-m','40','-A',UA,'-H','Accept-Language: en-US,en;q=0.9','-w','\n%{url_effective}',url],capture_output=True,text=True).stdout
    html,_,final=r.rpartition('\n')
    m=re.search(r'<script id="__NEXT_DATA__"[^>]*>(.*?)</script>',html,re.S)
    if not m: return dict(ok=False,final=final,len=len(html))
    d=json.loads(m.group(1))
    cache=next(find(d,'gdpClientCache'),None)
    if not cache: return dict(ok=False,final=final,note='no gdpClientCache (probably search page)')
    c=json.loads(cache) if isinstance(cache,str) else cache
    p=next(iter(c.values())).get('property') or {}
    ai=p.get('attributionInfo') or {}
    ph=[(h.get('date'),h.get('event'),h.get('price')) for h in (p.get('priceHistory') or [])[:4]]
    rf=p.get('resoFacts') or {}
    return dict(ok=True,final=final,address=f"{p.get('streetAddress')}, {p.get('city')}, {p.get('state')} {p.get('zipcode')}",
      status=p.get('homeStatus'),true_status=ai.get('trueStatus'),price=p.get('price'),dom=p.get('daysOnZillow'),beds=p.get('bedrooms'),baths=p.get('bathrooms'),
      sqft=p.get('livingArea'),lot=rf.get('lotSize') or p.get('lotAreaValue'),agent=ai.get('agentName'),phone=ai.get('agentPhoneNumber'),email=ai.get('agentEmail'),
      broker=ai.get('brokerName'),broker_phone=ai.get('brokerPhoneNumber'),mls=ai.get('mlsId'),lat=p.get('latitude'),lon=p.get('longitude'),hist=ph)
if __name__=='__main__':
    import sys;print(json.dumps(fetch(sys.argv[1]),indent=1,default=str))
