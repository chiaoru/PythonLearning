# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 19:53:28 2023

@author: USER
"""

# 華視新聞
import requests
from bs4 import BeautifulSoup

url = "https://news.cts.com.tw/real/index.html"

header = {
    
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }

data = requests.get(url, headers=header)

data.encoding = 'utf-8'
data = data.text

#print(data)

soup = BeautifulSoup(data, 'html.parser')

news = soup.find(id='newslist-top')

allnews = news.find_all('a')

for item in allnews:
    title = item.get('title')
    
    link = item.get('href')
    
    img = item.find('img')
    if not img == None:
        photo_url = img.get('data-src')
    else:
        photo_url = " "
        
    print(title)
    print('連結：',link)
    print('圖片位址：',photo_url)
    print()