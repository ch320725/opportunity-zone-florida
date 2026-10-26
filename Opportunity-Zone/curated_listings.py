# Hand-verified listing records for the 2026-10-26 scan (sources fetched/searched 2026-10-26).
# oz_status: IN OZ = point-in-polygon against 2010 OZ tract polygons (Census geocode or county parcel coords).
L=[]
def a(county,address,price,status,oz_status,oz_tract,source,url,beds='',baths='',sqft='',lot='',dom='',agent='',phone='',email='',notes='',prior_url=''):
    L.append(dict(county=county,address=address,list_price=price,status=status,oz_status=oz_status,oz_tract=oz_tract,
      beds=beds,baths=baths,sqft=sqft,lot_size=lot,days_on_market=dom,agent_name=agent,agent_phone=phone,agent_email=email,
      source=source,listing_url=url,notes=notes,prior_url=prior_url))
# ---------------- LEE ----------------
a('Lee','954 Capetown Ave, Lehigh Acres, FL 33974',19900,'Active','IN OZ','12071040308','realty.com','https://www.realty.com/land-listings/1058825217/954-Capetown-Ave-Lehigh-Acres-FL-33974',
  dom=182,agent='Fred Elliott (Coldwell Banker Preferred)',phone='239-357-7877 / office 239-369-6161',notes='Vacant residential lot',prior_url='https://www.realty.com/land-listings/1058825217/954-Capetown-Ave-Lehigh-Acres-FL-33974')
a('Lee','1022 Asther St E, Lehigh Acres, FL 33974',19900,'Active','IN OZ','12071040314','realty.com','https://www.realty.com/land-listings/1058811920/1022-Asther-St-E-Lehigh-Acres-FL-33974',
  dom=182,agent='Fred Elliott (Coldwell Banker Preferred)',phone='239-357-7877',notes='Vacant residential lot',prior_url='https://www.realty.com/land-listings/1058811920/1022-Asther-St-E-Lehigh-Acres-FL-33974')
a('Lee','933 Commodore St, Lehigh Acres, FL 33974',24900,'Active','IN OZ','12071040308','dream-coast-realty (MLS 2026019226)','https://www.dream-coast-realty.com/en/component/iproperty/property/2026019226-933-%20Commodore%20Street-Lehigh%20Acres?Itemid=101',
  agent='Coldwell Banker Preferred Properties',notes='Vacant lot',prior_url='https://www.dream-coast-realty.com/en/component/iproperty/property/2026019226-933-%20Commodore%20Street-Lehigh%20Acres?Itemid=101')
a('Lee','1048 Redbank Ave, Lehigh Acres, FL 33974',44900,'Active','IN OZ (parcel)','12071040308','Coldwell Banker (MLS 2026020470)','https://www.coldwellbankerhomes.com/fl/lehigh-acres/1048-redbank-ave/pid_71061770/',
  lot='0.5534 ac',agent='Patti North (Alliance Realty Group)',phone='(239) 281-3497',
  notes='BASELINE CORRECTION: 10-25 row showed $29,900 / MLS 2026019254 - that MLS is actually 385 McArthur Blvd. Real listing $44,900 (reduced from $49,900 on 2026-07-15), RS-1; owner ZYGMUNT CATHERINE S',prior_url='https://www.theguillettegroup.com/search/results/4sx2/')
a('Lee','385 McArthur Blvd, Lehigh Acres, FL 33974',29900,'Active','IN OZ','12071040314','MLS 2026019254 (Coldwell Banker Preferred)','',
  lot='0.30 ac',agent='Fred Elliott (Coldwell Banker Preferred)',phone='239-369-6161',notes='NEW this week (was mis-attributed to 1048 Redbank in baseline)')
a('Lee','850 Genoa Ave S, Lehigh Acres, FL 33974',17900,'Active','IN OZ','12071040308','MLS 2026020552 (Coldwell Banker Preferred)','',
  lot='0.23 ac',agent='Fred Elliott (Coldwell Banker Preferred)',phone='(239) 369-6161',notes='NEW; updated 2026-10-25')
a('Lee','540 Columbus Blvd S, Lehigh Acres, FL 33974',19900,'Active','IN OZ','12071040314','MLS 2026019210 (Coldwell Banker Preferred)','',
  lot='0.23 ac',agent='Fred Elliott (Coldwell Banker Preferred)',phone='(239) 369-6161',notes='NEW')
a('Lee','3428 Meadow Rd, Lehigh Acres, FL 33974',999999,'Active','IN OZ (parcel)','12071040308','Suncoast Realty Solutions (MLS 225083092)','',
  lot='3.21 ac',dom=309,agent='Key & Legacy Realty LLC (per Zillow)',notes='NEW to tracker; RS-1; owner CIANNA INVESTMENT PROPERTY LLC; 309 days on site')
a('Lee','3608 Sammy Watkins Ave, Fort Myers, FL 33916',525000,'Active','IN OZ (parcel)','12071000600','Coldwell Banker (MLS 2026042068) / Zillow','https://www.coldwellbankerhomes.com/fl/fort-myers/3608-sammy-watkins-ave/pid_74129372/',
  beds=8,baths=4,sqft=2600,lot='0.304 ac',dom=20,agent='Alec Burke; Justin Milcetich (LSI Companies Inc.)',
  notes='Quadplex 4x 2bd/1ba, built 1967, RS-7, listed 2026-10-06, opex $24,000; last sold 2019-07-23 $245,000; owner ARYX LLC',prior_url='https://www.loopnet.com/search/commercial-real-estate/fort-myers-fl/for-sale/')
a('Lee','3696 Dr Martin Luther King Jr Blvd, Fort Myers, FL 33916',1092000,'Active','IN OZ','12071000600','Crexi / TotalCommercial','https://www.crexi.com/properties/2712450/florida-3696-doctor-martin-luther-king-junior-boulevard',
  sqft=4200,lot='0.70 ac',dom=38,agent='Theresa M. Blauch-Mitchell, CCIM (Sperry Commercial Global Affiliates)',phone='(239) 265-2628',email='theresa@ccim.net',
  notes='Freestanding 1977 bldg, Commercial Intensive, 51k ADT, fenced yard; $260/SF; updated 2026-10-23',prior_url='https://www.loopnet.com/search/commercial-real-estate/fort-myers-fl/for-sale/')
a('Lee','203 Del Prado Blvd N, Cape Coral, FL 33909',799000,'Active','IN OZ','12071010302','MLS 2026034070 / Zillow','https://www.zillow.com/homedetails/203-Del-Prado-Blvd-N-Cape-Coral-FL-33909/447266613_zpid/',
  lot='0.705 ac',dom=75,agent='Properties in Paradise Real Estate, LLC',notes='NEW to tracker; zoning P; listed 2026-08-11; owner will carry')
a('Lee','3171 Dr Martin Luther King Jr Blvd, Fort Myers, FL 33916',850000,'Status unverified (LoopNet blocked)','IN OZ','12071000502','LoopNet 32029813 (search snippet only)','https://www.loopnet.com/Listing/3171-Dr-Martin-Luther-King-Blvd-Fort-Myers-FL/32029813/',
  lot='1.1 ac',agent='Mike Trivett (LSI Companies)',phone='239-940-3171 (per search snippet)',notes='Commercial Intensive land; site occupied by tire business; could not confirm still active')
a('Lee','1407 Lincoln Ave, North Fort Myers, FL 33903',139000,'Status unverified (LoopNet blocked)','IN OZ','12071020502','LoopNet 28893725 (search snippet only)','https://www.loopnet.com/Listing/1407-Lincoln-Ave-North-Fort-Myers-FL/28893725/',
  lot='0.53 ac',notes='Could not confirm still active')
a('Lee','7760 Bogart Dr, Fort Myers, FL 33917',2600000,'SOLD / stale','IN OZ','12071020300','LoopNet (prior)','https://www.loopnet.com/search/commercial-real-estate/fort-myers-fl/for-sale/',
  agent='Benny Spensieri',notes='Lee PA: sold 2026-01-28 for $1,800,000 to KW17 LLC (MLS 2025004247 closed). Removed from active list',prior_url='https://www.loopnet.com/search/commercial-real-estate/fort-myers-fl/for-sale/')
for addr,price,agent,dist in [('1001 Polk St, Fort Myers, FL 33916',950000,'Nick Hull; Austin Hull','~0.46 km from 12071000503'),
    ('2134-2136 Alicia St, Fort Myers, FL 33901',1631000,'Dror Attias','~0.09 km from 12071000600'),
    ('50 Mildred Dr, Fort Myers, FL 33901',800000,'Zachary Tillery; Colton Brausen',''),
    ('2249 Cleveland Ave, Fort Myers, FL 33901',995000,'Alec Salameh',''),
    ('3615 Central Ave, Fort Myers, FL 33901',3000000,'Jeff Forsythe',''),
    ('11118 S Cleveland Ave, Fort Myers, FL 33907',845000,'Stan Stouder, CCIM',''),
    ('5450-5460 5th Ave, Fort Myers, FL 33907',7200000,'Meidan Mike Magen; Astar Sakuri (Compass)',''),
    ('164 Pondella Rd, North Fort Myers, FL 33903',474900,'Gibson Eagle (Danholm Collection)','~0.5 km from 12071020502'),
    ('18031 State Road 31, North Fort Myers, FL 33917',5000000,'Jeff Forsythe',''),
    ('13400 Palm Beach Blvd, Fort Myers, FL 33905',3500000,'Tom Woodyard',''),
    ('4901 Buckingham Rd, Fort Myers, FL 33905',1799000,'Kelly Barnes; Ashlee Pendarvis',''),
    ('15855 Pine Ridge Rd, Fort Myers, FL 33908',500000,'Alec Burke',''),
    ('16231 Lee Rd, Fort Myers, FL 33912',2250000,'Nick Sweat (Gulf Shore Properties)',''),
    ('16001 Cintron Pl, Fort Myers, FL 33912',2250000,'Michael Maurer','')]:
    a('Lee',addr,price,'Not re-checked (LoopNet blocked)','NOT in OZ',dist,'LoopNet (prior)','https://www.loopnet.com/search/commercial-real-estate/fort-myers-fl/for-sale/',agent=agent,
      notes='Geocode check 2026-10-26: outside every OZ tract - reclassified as near-OZ reference',prior_url='https://www.loopnet.com/search/commercial-real-estate/fort-myers-fl/for-sale/')
# ---------------- COLLIER ----------------
a('Collier','W Main St & N 11th St, Immokalee, FL 34142',5500000,'Active','IN OZ','12021011400','RI Marketplace (Lee & Associates)','https://rimarketplace.com/listing/134238/land/immokalee/fl',
  lot='9.82 ac',agent='Felipe Arcila (Lee & Associates)',phone='239-402-3851',email='farcila@lee-associates.com',notes='LoopNet "Robert\'s Ridge" copy shows $4.5M - price conflict, confirm with broker',prior_url='https://rimarketplace.com/listing/134238/land/immokalee/fl')
a('Collier','602 W Main St, Immokalee, FL 34142','Call for price','Active','IN OZ','12021011400','Trinity Commercial Group brochure (2026-08) / CommercialSearch','https://trinitycre.com/wp-content/uploads/2026/08/Brochure-602-W-Mainstreet-Immokalee.pdf',
  sqft=6989,lot='0.3 ac',agent='Ty Hensley (Trinity Commercial Group)',notes='NEW; retail bldg, C-4, ~22,000 VPD; price not published')
a('Collier','1312 15th St N, Immokalee, FL 34142',1500000,'Status unverified (LoopNet blocked)','IN OZ','12021011400','LoopNet 32557368','https://www.loopnet.com/Listing/1312-15th-St-N-Immokalee-FL/32557368/',prior_url='https://www.loopnet.com/Listing/1312-15th-St-N-Immokalee-FL/32557368/')
a('Collier','State Road 29, Immokalee, FL 34142','','Status unverified (LoopNet blocked)','Unverified (no address)','','LoopNet 18365094','https://www.loopnet.com/Listing/State-Road-29-Immokalee-FL/18365094/',prior_url='https://www.loopnet.com/Listing/State-Road-29-Immokalee-FL/18365094/')
a('Collier','10001 Tamiami Trl E, Naples, FL 34113',6500000,'For LEASE verified ($15/SF NNN); sale status unverified','IN OZ','12021010802','CommercialSearch (lease) / LoopNet 34581258 (sale, blocked)','https://www.commercialsearch.com/commercial-property/us/fl/naples/rarely-available-naples-location/',
  sqft=24833,lot='1.77 ac',agent='Brock Rasmussen, SIOR (Lee & Associates)',notes='NEW; former Lenny\'s Furniture, C-4, 197 ft on US-41; sale price seen as $6.5M (LoopNet) and $5.3M (other snippet) - conflicting')
a('Collier','3933 Tollhouse Dr, Naples, FL 34114',9606022,'Active','NOT in OZ','~1.6 km from nearest OZ','realmo','https://realmo.com/listing/3933-tollhouse-dr-naples-fl-34114/9116493',
  dom=215,agent='David Bartley Sr (Bartley Realty)',phone='(239) 596-1181',notes='Reclassified: not in an OZ tract',prior_url='https://realmo.com/listing/3933-tollhouse-dr-naples-fl-34114/9116493')
a('Collier','3893 Mannix Dr #529, Naples, FL 34114',425000,'Likely removed (URL redirects to search)','NOT in OZ','','realmo','https://realmo.com/listing/529-3893-mannix-dr-naples-fl-34114/12946901',
  agent='Matthew Stepan PA (Premier Commercial)',prior_url='https://realmo.com/listing/529-3893-mannix-dr-naples-fl-34114/12946901')
# ---------------- CHARLOTTE ----------------
a('Charlotte','3092 Tamiami Trl, Port Charlotte, FL 33952',900000,'Status unverified (LoopNet blocked; still indexed)','IN OZ','12015020700','LoopNet 34903575','https://www.loopnet.com/Listing/3092-Tamiami-Trl-Port-Charlotte-FL/34903575/',prior_url='https://www.loopnet.com/Listing/3092-Tamiami-Trl-Port-Charlotte-FL/34903575/')
a('Charlotte','2901 Placida Rd, Englewood, FL 34224',999999,'Active','IN OZ','12015030401','raveis (MLS A4665839)','',
  sqft=1774,lot='0.5 ac',dom=373,notes='NEW to tracker; restaurant; reduced from $1,295,000 on 2026-03-20')
a('Charlotte','2931 Placida Rd, Englewood, FL 34224',2500000,'Active','IN OZ','12015030401','MLS A4665752 (keysofsarasota / BHHS / LoopNet 33099386)','https://www.keysofsarasota.com/property/2931-placida-road-englewood-fl-34224-a4665752',
  sqft=20940,lot='0.72 ac',dom=400,agent='Virginia Fey (Bright Realty)',phone='941-587-9772 / 941-552-6036',email='virginiafey59@gmail.com',notes='NEW; signalized corner Placida/San Casa, CG + MF bonus parcel; listed 2025-09-20; sqft field as reported by MLS')
a('Charlotte','2900 Placida Rd, Englewood, FL 34224',1100000,'Pending','IN OZ','12015030401','raveis (MLS A4699827)','',notes='NEW; under contract')
a('Charlotte','3060 Placida Rd, Englewood, FL 34224',1950000,'Status unverified (Elliman blocked)','IN OZ','12015030401','Douglas Elliman D6144764','',sqft=9000,lot='3 ac')
a('Charlotte','2440 Placida Rd, Englewood, FL 34224',625000,'Listed (page schema says OutOfStock - confirm)','IN OZ','12015030401','MSC Commercial','',lot='1.24 ac',agent='G. River West (MSC Commercial)',notes='CT zoning; page updated 2026-10-18')
a('Charlotte','12691 State Road 31, Punta Gorda, FL 33982',750000,'Active','IN OZ','12015010100','MLS 224014187','',lot='10 ac',dom=651,agent='NRT Commercial LLC (per Zillow)',notes='NEW to tracker; RV-park use non-conforming')
a('Charlotte','21202-21234 Olean Blvd Unit 2S, Port Charlotte, FL 33952',337000,'Active (stale-risk: Compass last updated 2024)','IN OZ','12015020700','Compass (MLS C7486325)','',
  sqft=1975,dom=1015,agent='Shannon Gadbois (Thomas Ryan RE)',notes='2 commercial condos, CG')
a('Charlotte','4732 Tamiami Trl, Port Charlotte, FL 33980',2150000,'Not re-checked (Elliman blocked)','NOT in OZ','','Douglas Elliman','https://www.elliman.com/listing/4732-tamiami-trl-port-charlotte-fl-33980/32120039',prior_url='https://www.elliman.com/listing/4732-tamiami-trl-port-charlotte-fl-33980/32120039')
a('Charlotte','16070 Tamiami Trail, Punta Gorda, FL 33955',1890000,'Active','NOT in OZ','','Suncoast Realty Solutions','https://www.suncoastrealtysolutions.com/realestate/details/97314918/16070-tamiami-trail-punta-gorda-fl-33955',
  dom=78,agent='Jeffrey Wernsing (Suncoast)',phone='239-333-7941',notes='parcel 422430201001, owner WREX GROUP LLC',prior_url='https://www.suncoastrealtysolutions.com/realestate/details/97314918/16070-tamiami-trail-punta-gorda-fl-33955')
a('Charlotte','10000 Tamiami Trail, Punta Gorda, FL 33950',12999990,'Active','NOT in OZ','','Suncoast Realty Solutions','https://www.suncoastrealtysolutions.com/realestate/details/38360460/10000-tamiami-trail-punta-gorda-fl-33950',
  dom=172,agent='Jeffrey Wernsing (Suncoast)',phone='239-333-7941',notes='HC zoning; parcel 412321151008 RL TREWORGY LLC; 10/13 "reduction" of -0.0%',prior_url='https://www.suncoastrealtysolutions.com/realestate/details/38360460/10000-tamiami-trail-punta-gorda-fl-33950')
a('Charlotte','490 Tamiami Trail, Port Charlotte, FL 33953',390000,'Active','NOT in OZ','','Coldwell Banker','https://www.coldwellbankerhomes.com/fl/port-charlotte/490-tamiami-trail/pid_71436949/',
  agent='Re/Max Harbor Realty',notes='BASELINE CORRECTION: price was already $390,000 (reduced 2026-08-21); baseline showed $400,000',prior_url='https://www.coldwellbankerhomes.com/fl/port-charlotte/490-tamiami-trail/pid_71436949/')
a('Charlotte','1900 Tamiami Trail #C-D, Punta Gorda, FL 33950',1800000,'Active','NOT in OZ','','Coldwell Banker','https://www.coldwellbankerhomes.com/fl/punta-gorda/1900-tamiami-trail-c/pid_72321817/',
  dom=115,agent='Chris Coultas (Five Star Realty)',phone='(239) 201-9999',prior_url='https://www.coldwellbankerhomes.com/fl/punta-gorda/1900-tamiami-trail-c/pid_72321817/')
