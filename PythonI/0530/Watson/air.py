# -*- coding: utf-8 -*-
"""
Created on Tue May 30 21:04:14 2023

@author: USER
"""

import requests

url = "https://data.epa.gov.tw/api/v2/aqx_p_432?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=ImportDate%20desc&format=JSON"


data = requests.get(url).text

print(data)