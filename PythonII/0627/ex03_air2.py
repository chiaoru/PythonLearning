# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 20:01:14 2023

@author: USER
"""

# 環保署 AQI JSON

import requests
import json

url = "https://data.epa.gov.tw/api/v2/aqx_p_432?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=ImportDate%20desc&format=JSON"

data = requests.get(url).text

air = json.loads(data) # json 格式
air = air['records'] # 將air指派給主要的資料 key->records

county = {}

for row in air:
    
    area = county.get(row['county'], None)
    
    if area == None:
        temp = list()
        
        sitedict = dict()
        sitedict['sitename'] = row['sitename']
        sitedict['aqi'] = row['aqi']
        temp.append(sitedict)
        
        county[row['county']] = temp
        
    else:
        sitedict = dict()
        sitedict['sitename'] = row['sitename']
        sitedict['aqi'] = row['aqi']
        area.append(sitedict)
        
#print(county)
    
for row in county:
    #print(row)
    print(row, "的站台有:", end=" ")
    
    for site in county[row]:
        print(site['sitename'], end= " ")

    print()


