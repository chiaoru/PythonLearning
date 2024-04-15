# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 21:28:09 2023

@author: USER
"""

import requests
import json

url = "https://24h.pchome.com.tw/onsale/v5/data/data.json"

header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }

pchome = requests.get(url, headers=header).text

data = json.loads(pchome)

onsale = data['OnsaleJson']

"""
for item in onsale:
    if item['BlockId'] == 1:
        print("3C")
        
        goods = item['Nodes']
        for p in goods:
            title = p['Img']['Title']
            price = p['Link']['Text6']
            onsale = p['Link']['Text2']
            photo = 'https://fs-c.ecimg.tw/' + p['Img']['Src']
            link = p['Link']['Url']
            if not ('https:' in link):
                link = 'https:' + link
            
            print(title)
            print("原價：", price)
            print("特價：", onsale)
            print("連結：", link)
            print("照片：", photo)
            print()
            
            
    elif item['BlockId'] == 2:
        print('-'*30)
        print("家電")
        
        goods = item['Nodes']
        for p in goods:
            title = p['Img']['Title']
            price = p['Link']['Text6']
            onsale = p['Link']['Text2']
            photo = 'https://fs-c.ecimg.tw/' + p['Img']['Src']
            link = 'https:' + p['Link']['Url']
            
            print(title)
            print("原價：", price)
            print("特價：", onsale)
            print("連結：", link)
            print("照片：", photo)
            print()
        
        
    elif item['BlockId'] == 3:
        print('-'*30)
        print("日常")
        
        goods = item['Nodes']
        for p in goods:
            title = p['Img']['Title']
            price = p['Link']['Text6']
            onsale = p['Link']['Text2']
            photo = 'https://fs-c.ecimg.tw/' + p['Img']['Src']
            link = p['Link']['Url']
            if not ('https:' in link):
                link = 'https:' + link
            
            print(title)
            print("原價：", price)
            print("特價：", onsale)
            print("連結：", link)
            print("照片：", photo)
            print()
            
"""            
# 當程式碼大多重複時可將重複的程式碼往外丟
for item in onsale:
    if item['BlockId'] == 1:
        print("3C")
    elif item['BlockId'] == 2:
        print('-'*30)
        print("家電")
    elif item['BlockId'] == 3:
        print('-'*30)
        print("日常")
    else:
        continue
    
    goods = item['Nodes']
    for p in goods:
        title = p['Img']['Title']
        price = p['Link']['Text6']
        onsale = p['Link']['Text2']
        photo = 'https://fs-c.ecimg.tw/' + p['Img']['Src']
        link = 'https:' + p['Link']['Url']

            
        print(title)
        print("原價：", price)
        print("特價：", onsale)
        print("連結：", link)
        print("照片：", photo)
        print()
    
        
        
        
        
        