# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 18:55:18 2023

@author: USER
"""

import requests
from bs4 import BeautifulSoup

url = "https://tip.railway.gov.tw/tra-tip-web/tip/tip001/tip112/querybystation"

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }

param = {
    '_csrf': 'f9a851d2-8565-4312-8f4a-2ac7e42b6640',
'rideDate': '2023/07/18',
'station': '3300-臺中'
    }

# 重點 POST
data = requests.post(url, headers=header, data=param).text # data= 是屬於post帶參數的方式

soup = BeautifulSoup(data, 'html.parser')

direct = soup.find(id='tab1')
retrograde = soup.find(id='tab2')

direct_tr = direct.find_all('tr')
retrograde_tr = retrograde.find_all('tr')

direct_tr = direct_tr[1:]
retrograde_tr = retrograde_tr[1:]

# 方式二：也可抓td

print("順行")
for item in direct_tr:
    tds = item.find_all('td')
    print("車種車次：",tds[0].text.strip().replace('\n', ''))
    print("出發時間：",tds[1].text.strip())
    print("終點站：",tds[2].text.strip())
    print("服務：",tds[3].text.strip())
    print()
    
print("-"*30)
print("逆行")
for item in retrograde_tr:
    tds = item.find_all('td')
    print("車種車次：",tds[0].text.strip().replace('\n', ''))
    print("出發時間：",tds[1].text.strip())
    print("終點站：",tds[2].text.strip())
    print("服務：",tds[3].text.strip())
    print()
    


