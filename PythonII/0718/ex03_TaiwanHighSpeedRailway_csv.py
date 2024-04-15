# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 20:02:35 2023

@author: USER
"""

# 高鐵時刻表，存成csv
import requests
import json
import csv

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

number = list()
startTime = list()
endTime = list()
duration = list()
stat = list()

for item in thsr:
    number.append(item['TrainNumber'])
    startTime.append(item['DepartureTime'])
    endTime.append(item['DestinationTime'])
    duration.append(item['Duration'])
    
    st = list()
    for station in item['StationInfo']:
        if station['Show'] == True:
            stat.append(station['StationName'])
    st.append(stat)
    
print(stat)  

fileName = "thsr.csv"
with open(fileName, 'w', newline='') as fObj:
    csvWrite = csv.writer(fObj)
    csvWrite.writerow(['車次', '出發時間', '旅行時間','抵達時間', '停靠站'])
    for i in range(len(number)):
        csvWrite.writerow([number[i], startTime[i], duration[i], endTime[i]])
    print('存檔完成!')
    
    
    
    
    
