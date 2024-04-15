# -*- coding: utf-8 -*-
"""
Created on Tue May 30 20:56:06 2023

@author: USER
"""

import json
import requests

def getAQI():

    url = "https://data.epa.gov.tw/api/v2/aqx_p_432?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=ImportDate%20desc&format=JSON"

    datas = requests.get(url).text
    
    data = json.loads(datas)
    
    air = data['records']

    msg=""  
    i = 0
    
    for item in air:
        msg += item['sitename'] + "-" + item['aqi'] + "\n"
        i += 1
        
        if i == 6:
            break
        
    return msg