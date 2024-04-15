# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 19:07:04 2023

@author: USER
"""

import requests
from bs4 import BeautifulSoup

import db

url = "https://supertaste.tvbs.com.tw/food"

header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }

foods = requests.get(url, headers=header)
foods.encoding = 'utf-8'
foods = foods.text

soup = BeautifulSoup(foods, 'html.parser')

allFoods = soup.find('div', class_='article__content')

a = allFoods.find_all('a')

for item in a:
    title = item.find('h3').text.strip()
    post_date = item.find('span').text.strip()
    
    link = item.get('href')
    if not ('http' in link):
        link = "https://supertaste.tvbs.com.tw" + link

    img = item.find('img').get('data-original')
    
    sql = "select * from food where link='{}'".format(link)
    db.cursor.execute(sql)
    db.connect.commit() # 確保即時更新
    
    if db.cursor.rowcount == 0:

        sql = "insert into food(name, photo_url, link, create_date) values(%s,%s,%s,%s)"
        #ProgrammingError: Not enough parameters for the SQL statement
        
        db.cursor.execute(sql,[title, img, link, post_date])
        db.connect.commit()
            
db.connect.close()