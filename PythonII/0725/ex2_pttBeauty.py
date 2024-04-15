# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 19:33:03 2023

@author: USER
"""

import requests
from bs4 import BeautifulSoup

url = "https://www.ptt.cc/bbs/Beauty/index.html"

header = {
    
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'Cookie':'over18=1'    }

soup = BeautifulSoup('', 'html.parser')

for i in range(1,6):
    
    if i > 1:
        lastPage = soup.find_all('a',class_='btn wide') # 串列: 最舊 上頁 下頁 最新
        url = "https://www.ptt.cc" + lastPage[1].get('href') 
        
    data = requests.get(url, headers=header).text
    
    soup = BeautifulSoup(data, 'html.parser')
    
    beauty = soup.find_all('div', class_='r-ent')
    
    for row in beauty:
        
        a = row.find('a')
        if not (a == None):
        
            link = "https://www.ptt.cc" + row.find('a').get('href')          
            title = row.find('a').text
            print(title)
            print(link)
            print()
    
