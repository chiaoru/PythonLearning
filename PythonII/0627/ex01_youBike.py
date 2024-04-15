# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 19:24:28 2023

@author: USER
"""

# 新北市 YouBike JSON

import requests
import json

url = "https://data.ntpc.gov.tw/api/datasets/71cd1490-a2df-4198-bef1-318479775e8a/json?size=100"

data = requests.get(url).text # 抓下來是串流stream，須轉成文字text

#print(data) # 確保抓下來有資料，之後再刪除
    
bike = json.loads(data)

#print(data) # json 格式(字典)

for row in bike:
    print('站名：', row['sna'])
    print('可借：', row['sbi'])
    print('可停：', row['bemp'])
    print()
    


