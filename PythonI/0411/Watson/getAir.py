# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 18:47:17 2023

@author: USER
"""

import requests
import json

url = "https://data.epa.gov.tw/api/v2/aqx_p_432?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=ImportDate%20desc&format=JSON"
air = requests.get(url).text


data = json.loads(air)

items = data['records']

for row in items:
    print(row)
    print()

