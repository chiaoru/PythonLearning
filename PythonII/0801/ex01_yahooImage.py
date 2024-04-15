# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 19:11:23 2023

@author: USER
"""

import requests
from bs4 import BeautifulSoup
import json

url = "https://tw.buy.yahoo.com/search/product?p=switch"

header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }

data = requests.get(url, headers=header).text
soup = BeautifulSoup(data, 'html.parser')


products = soup.find_all('a', class_="sc-1drl28c-1 hcbDur")

allimg = soup.find(id='isoredux-data').get('data-state')

images = json.loads(allimg)
pimg = images['search']['ecsearch']['hits']

# 將JSON檔案抓出再放到json parser裡面解析，之後再分解出圖片位址
fn = 'yahooImg.txt'
with open(fn, 'w', encoding='utf-8') as fO:
    fO.write(allimg)

for item in products:
    title = item.find('img').get('alt')
    link = item.get('href') 
    
    for row in pimg:
        yaphoto = ""
        if link == row['ec_item_url']:
            yaphoto = row['ec_image']
            break
    
    print("標題：",title)

    allprice = item.find('div', class_="sc-1ap2njs-0 dPpkAj")
    price = allprice.find_all('span', class_="eCzBYn")
    #print("特價：",price[0].text)
    
    intprice = price[0].text.replace('$', '')
    intprice = intprice.replace(',', '')
    
    print("特價：",intprice) # 整數才可在資料庫中被比較作分析
    
    if len(price) == 2:
        print("原價：",price[1].text)
        
    print("圖片：", yaphoto)
    print("連結：",link)
    print()