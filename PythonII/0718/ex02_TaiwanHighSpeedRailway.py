# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 20:02:35 2023

@author: USER
"""

# 高鐵時刻表
import requests
import json

url = "https://www.thsrc.com.tw/TimeTable/Search"

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }

param = {
    'SearchType': 'S',
    'Lang': 'TW',
    'StartStation': 'NanGang',
    'EndStation': 'ZuoYing',
    'OutWardSearchDate': '2023/07/18',
    'OutWardSearchTime': '20:00',
    'ReturnSearchDate': '2023/07/18',
    'ReturnSearchTime': '20:00'
    }

thsr = requests.post(url, headers=header, data=param).text
data = json.loads(thsr)

thsr = data['data']['DepartureTable']['TrainItem']

for item in thsr:
    print("車次：", item['TrainNumber'])
    print("旅行時間：", item['Duration'])
    print("出發時間：", item['DepartureTime'])
    print("抵達時間：", item['DestinationTime'])
    print("停靠站：", end='')
    for station in item['StationInfo']:
        if station['Show'] == True:
            print(station['StationName'], end=' ')
    print()
    print()
    
    
