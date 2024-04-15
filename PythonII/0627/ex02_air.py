# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 19:38:54 2023

@author: USER
"""

# 環保署 AQI

import requests
import json

url = "https://data.epa.gov.tw/api/v2/aqx_p_432?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=ImportDate%20desc&format=JSON"

data = requests.get(url).text

air = json.loads(data) # json 格式
air = air['records'] # 將air指派給主要的資料 key->records

for row in air:
    print("站台：", row['sitename'])
    print("縣市：", row['county'])
    print("AQI：", row['aqi'])
    
    aqi = int(row['aqi'])
    if aqi < 50:
        print("空氣品質良好")
    elif aqi <100:
        print("空氣品質普通")
    else:
        print("空氣品質危害")
    
    print()