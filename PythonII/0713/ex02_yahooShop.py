# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 19:56:23 2023

@author: USER
"""

import requests
from bs4 import BeautifulSoup

url = "https://tw.buy.yahoo.com/search/product"

header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }

param = {}
p = input("請輸入欲搜尋的產品名稱：")
param['p'] = p

yahoo = requests.get(url, headers=header, params=param).text

soup = BeautifulSoup(yahoo, 'html.parser')

products = soup.find_all('a', class_="sc-1drl28c-1 hcbDur")

for item in products:
    title = item.find('img').get('alt')
    link = item.get('href') 
    print("標題：",title)

    allprice = item.find('div', class_="sc-1ap2njs-0 dPpkAj")
    price = allprice.find_all('span', class_="eCzBYn")
    #print("特價：",price[0].text)
    
    intprice = price[0].text.replace('$', '')
    intprice = intprice.replace(',', '')
    
    print("特價：",intprice) # 整數才可在資料庫中被比較作分析
    
    if len(price) == 2:
        print("原價：",price[1].text)
    
    print("連結：",link)
    print()
    
    # img 因為 java script 觸發的關係 需等待才能被抓取



