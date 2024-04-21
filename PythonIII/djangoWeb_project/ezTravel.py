#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 21:03:12 2023

@author: kate
"""

# 易遊網
import requests
from bs4 import BeautifulSoup
import re
import time
import db
from datetime import datetime

today = datetime.today()
now = today.strftime('%Y-%m-%d')

area = input('請輸入想搜尋的旅行地點：')

for i in range(1,4):
    # 以關鍵字搜尋
    url = 'https://vacation.eztravel.com.tw/pkgfrn/keywords/'
    
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15'
        
        }
    
    param = {
        'q': '瑞士',
        'departure': 'TPE',
        'avbl': '1',
        'depDateFrom': '20231122',
        'depDateTo': '20240518',
        'page': '1'
        }
    
    param['page'] = i
    
    param['q'] = area
    
    data = requests.get(url, headers=header, params=param).text
    
    soup = BeautifulSoup(data,'html.parser')
    
    tours = soup.find(id='listTable')
    
    tour = tours.find_all('li', class_='list-item')
    
    for row in tour:
        title = row.find('h2', class_='prod-title').text

        img = row.find('img', class_='list-item-img').get('src')
        
        link = row.find('a').get('href')
        
        content = row.find('div', class_='keywords-box').text
        price =row.find('span', class_='text-price').text
        price = re.findall('([A-Z0-9]+)', price)
        price = price[0] + price[1]
        #depDates = row.find_all('div', class_='sale-dt') #抓出空值
        
        print(title)
        #print(content)
        print(price)
        #print(depDates)
        print(img)
        print(link)
        print()

        platform = '易遊網'
        depDate = '詳情請進內頁'
        
        sql = "select * from tours where platform='{}' and title='{}' and depDate='{}'".format(platform, title, depDate)
        db.cursor.execute(sql)
        result = db.cursor.fetchone()
        if result == None:
            sql = "insert into tours(platform, area, title, price, depDate, img, link, createDate) values('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(platform, area, title, price, depDate, img, link, now)
            db.cursor.execute(sql)
            db.connect.commit()
            
        elif result != None:
            sql = "update tours set price='{}' where title='{}'".format(price, title)
            db.cursor.execute(sql)
            db.connect.commit()
        
        time.sleep(1)
            
#db.connect.close()
