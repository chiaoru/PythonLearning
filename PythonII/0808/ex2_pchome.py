# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 19:19:54 2023

@author: USER
"""

import requests
#from bs4 import BeautifulSoup
import json
import time

import db
import datetime

url = "https://ecshweb.pchome.com.tw/search/v3.3//all/results"

header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
        }

param = {
    'q': '可口可樂',
    'page': '1',
    'sort': 'sale/dc'
    }

p = input("請輸入欲搜尋的商品：")
param['q']=p

for i in range(1, 6):
    param['page'] = str(i)
    pchome = requests.get(url, headers=header, params=param).text
    data = json.loads(pchome)

    products = data['prods']

    for item in products:
        title = item['name']
        price = item['originPrice']
        onsale = item['price']
        photo = 'https://cs-a.ecimg.tw/' + item['picB']
        link = 'https://24h.pchome.com.tw/prod/' + item['Id']
        describe = item['describe']
        
        sql = "select * from product where platform='PChome' and link='{}'".format(link)
        db.cursor.execute(sql)
        
        if db.cursor.rowcount == 0:
            today = datetime.datetime.today() # 時間格式
            now = today.strftime('%Y-%m-%d') #yyyymmdd
            sql = "insert into product(platform,title,photo_url,link,price,onsale,create_date) values(%s,%s,%s,%s,%s,%s,%s)"
            db.cursor.execute(sql,['PChome',title, photo, link, price, onsale, now])
            db.connect.commit()
          
        
        
    print('-'*40)
    
    time.sleep(1)
    

