# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 19:07:04 2023

@author: USER
"""

import requests
from bs4 import BeautifulSoup

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
        
    print("標題：",title)
    print("日期：",post_date)
    print("連結：",link)
    print("圖片：",img)
    print()
    