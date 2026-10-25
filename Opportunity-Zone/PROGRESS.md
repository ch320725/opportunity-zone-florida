# Opportunity Zone progress (2026-10-25)
## OZ tracts (2018 designated QOZs, 2010 tract GEOIDs) — oz-tracts.json
Source: CDFI/Treasury national OZ layer https://services.arcgis.com/VTyQ9soqVukalItT/ArcGIS/rest/services/Opportunity_Zones/FeatureServer/13
- Lee (12071): 15 — 12071000502, 000503, 000600, 001910, 010201, 010302, 010307, 020201, 020300, 020502, 040122, 040308, 040313, 040314, 050103
- Collier (12021): 5 — 12021010411, 010802, 011205, 011301, 011400
- Charlotte (12015): 3 — 12015010100, 020700, 030401
Lee local OZ layer (7 named areas, no GEOIDs): https://services2.arcgis.com/LvWGAAhHwbCJ2GMP/arcgis/rest/services/Opportunity_Zones/FeatureServer/0
## Parcel endpoints (working)
- Lee: https://gismapserver.leegov.com/gisserver910/rest/services/DataExplorer/Parcels/MapServer/0 (owner, JUST/ASSESSED, ZONING, GISACRES, S_1..S_4 sales, DORCODE/LANDUSEDES). Alt: .../Layers/ParcelAddress/MapServer/0
- Collier + Charlotte: FDOR statewide cadastral https://services9.arcgis.com/Gh9awoU677aKree0/arcgis/rest/services/Florida_Statewide_Cadastral/FeatureServer/0 (OWN_NAME, JV, AV_NSD, LND_SQFOOT, SALE_PRC1/YR1/MO1, DOR_UC; NO zoning)
- Charlotte alt w/ zoning: https://www45.swfwmd.state.fl.us/arcgis12/rest/services/BaseVector/parcel_search/MapServer/1 (not yet pulled)
- Collier official: CSV/shapefile downloads only https://www.collierappraiser.com/Main_Data/DataDownloads.html (no public REST found); third-party FS gis.cdrmaguire.com (not used)
## Method
Spatial intersect of each OZ tract polygon; DOR codes 00,10,11-39,40-49,70; >=0.25 ac; sorted by acreage desc, top 60 per tract. corridor_notes = street-name match on site address.
## Rows: Lee 504, Collier 266, Charlotte 180 (see pull_log.txt). Script: pull.py
## Gaps: Collier/Charlotte zoning blank; sale date month-level only (FDOR); tracts capped at 60 rows; no corridor-buffer queries outside OZs yet.
