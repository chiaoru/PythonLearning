# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 21:03:45 2023

@author: USER
"""

# 台銀即時匯率
import requests
from bs4 import BeautifulSoup

url = "https://rate.bot.com.tw/xrt?Lang=zh-TW"

header = {
    
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }

data = requests.get(url, headers=header)

data.encoding = 'utf-8'
data = data.text

#print(data)

soup = BeautifulSoup(data, 'html.parser')

rate = soup.find('table')

allRate = rate.find('tbody')
trs = allRate.find_all('tr')

for item in trs:
    tds = item.find_all('td') # td 每一欄
    currency = tds[0].text.strip() # strip 去前後空白
    currency = currency.split() # 分割字串，為了去文字之間的空白
    
    print(currency[0], currency[1])
    print(tds[1].text.strip())
    print(tds[2].text.strip())
    print(tds[3].text.strip())
    print(tds[4].text.strip())
    print()


# HW 解玉山銀行的即時匯率