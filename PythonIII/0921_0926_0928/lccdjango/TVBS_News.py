# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 18:56:00 2023

@author: USER
"""

import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time
import re
import db

url = 'https://news.tvbs.com.tw/realtime'

data = requests.get(url).text

soup = BeautifulSoup(data, 'html.parser')

newslist = soup.find('div', class_='news_list')
allnews = newslist.find('div', class_='list')
news = allnews.find_all('li')


for item in news:
    a_data = item.find('a')
    if not(a_data == None):
        
        img = a_data.find('img').get('data-original')
            
        title = a_data.find('h2').text
        
        today = datetime.today()
        today = today.strftime('%Y-%m-%d')
        
        link = 'https://news.tvbs.com.tw/' + a_data.get('href')
        content = requests.get(link).text
        soupC = BeautifulSoup(content, 'html.parser')
        newsinfo = soupC.find(id='news_detail_div')
        info = newsinfo.text
        info = info.replace('\n', '')
        
        authorinfo = soupC.find('div', class_='author').text
        timeinfo = re.findall("([0-9]+)", authorinfo)
        timeinfo = timeinfo[0] + '-' + timeinfo[1] + '-' + timeinfo[2] + '-'+ timeinfo[3] 
        
        sql = "select * from news where title='{}'".format(title)
        db.cursor.execute(sql)
        result = db.cursor.fetchone()
        if result == None:
            sql = "insert into news(title, content, photo_url, c_date) values('{}', '{}', '{}', '{}')".format(title, info, img, timeinfo)
            db.cursor.execute(sql)
            db.connect.commit()
            
    time.sleep(1)
            
db.connect.close()

      