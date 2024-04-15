# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 21:28:30 2023

@author: USER
"""

import requests
import json

url = "https://opendata.hccg.gov.tw/OpenDataFileHit.ashx?ID=48DEDBDAC3A31FC6&u=77DFE16E459DFCE3F5CEA2F931E333F7E23D5729EF83D5F20744125E844FB27044F9892E6F09372518441B3BB84260426ADE242A57DFB9E8C9A50C50134F4F47"
data = requests.get(url).text


area = json.loads(data)

city = area['retVal']
for item in city:
    print(item['sna'])
    
    print(item['ar'])
    print(item['sbi'])
    print(item['bemp'])
    print()