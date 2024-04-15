# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 21:31:39 2023

@author: USER
"""

import requests
import json

url = "https://opendata.hccg.gov.tw/OpenDataFileHit.ashx?ID=48DEDBDAC3A31FC6&u=77DFE16E459DFCE3F5CEA2F931E333F7E23D5729EF83D5F20744125E844FB27044F9892E6F09372518441B3BB84260426ADE242A57DFB9E8C9A50C50134F4F47"

data = requests.get(url).text 
#print(data)

shinchu = json.loads(data) # 載入 json資料

info = shinchu['retVal']

for item in info:
    print("站名",item['sna'])
    print("地址", item['ar'])
    print("可借", item['sbi'])
    print("可停", item['tot'])
    print()