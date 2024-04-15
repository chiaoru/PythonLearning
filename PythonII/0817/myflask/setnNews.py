# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 18:47:52 2023

@author: USER
"""

import requests
from bs4 import BeautifulSoup

# 可即時抓取，不存於資料庫
# 三立新聞
url = "https://www.setn.com/ViewAll.aspx?PageGroupID=0"

header = {
    
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }

data = requests.get(url, headers=header).text

#print(data)

soup = BeautifulSoup(data, 'html.parser')

news = soup.find(id="NewsList")

allNews = news.find_all('h3') # 抓取所有的h3 成為一組串列

for item in allNews: # 用迴圈跑出每一筆資料
    link = item.find('a').get('href') # 抓屬性
    if not ('http' in link): # 確保連結的完整性
        link = 'https://www.setn.com/' + link
    
    title = item.find('a').text # 抓文字
    
    print("標題：", title)
    print("連結：", link)
    
    print()