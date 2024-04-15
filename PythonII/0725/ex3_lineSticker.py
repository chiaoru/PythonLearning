# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 21:02:46 2023

@author: USER
"""

import requests
from bs4 import BeautifulSoup
import json
import urllib.request # 抓取圖片用的

url = 'https://store.line.me/stickershop/product/26393/zh-Hant'

header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
}

data = requests.get(url, headers=header).text
soup = BeautifulSoup(data, 'html.parser')
li = soup.find_all('li', class_='mdCMN09Li FnStickerPreviewItem animation-sticker')

i = 100
for row in li:
    img = row.get('data-preview')
    line = json.loads(img)
    urllib.request.urlretrieve(line['staticUrl'], str(i)+".png") 
    # urllib.request.urlretrieve(來源, 目的地)
    i += 1