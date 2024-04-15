# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 19:13:49 2023

@author: USER
"""

from selenium import webdriver

from bs4 import BeautifulSoup

import time

driverpath = "c:\webdriver\chromedriver.exe" # webdriver指向位置
driver = webdriver.Chrome(driverpath) # 用chrome driver去跑所在路徑

url = "https://tw.buy.yahoo.com/search/product?p=switch"

driver.implicitly_wait(3) # 背景等待時間 3秒 (如抓取資料時間不夠再延長)
driver.get(url)

# 拉取網頁畫面
height = 800

for i in range(5):
    driver.execute_script('window.scrollTo(0, {})'.format(height))
    time.sleep(1)
    height += 800
    
soup = BeautifulSoup(driver.page_source, 'html.parser')


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