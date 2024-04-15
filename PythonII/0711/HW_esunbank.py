#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 01:02:58 2023

@author: kate
"""

import requests
from bs4 import BeautifulSoup

url = "https://www.esunbank.com/zh-tw/personal/deposit/rate/forex/foreign-exchange-rates"

header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15'
    }

data  = requests.get(url, headers=header)
data.encoding = 'utf-8'
data = data.text

soup = BeautifulSoup(data, 'html.parser')

rate = soup.find(id='exchangeRate')

allRate = rate.find_all('tr')
trs = allRate[2:]

for i in range(30):
    
    currency = trs[i].text.strip().split()
    if len(currency)>3:
        print(currency[0] + " " + currency[1])
        print("  即期匯率：")
        print("    買入：", currency[4])
        print("    賣出：", currency[5])
        print("  網銀/APP優惠：")
        print("    買入：", currency[6])
        print("    賣出：", currency[7])
        if len(currency) > 8:
            print("  現金匯率：")
            print("    買入：", currency[8])
            print("    賣出：", currency[9])
        print()
 

