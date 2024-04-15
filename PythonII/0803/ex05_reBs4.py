# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 20:18:29 2023

@author: USER
"""

import re
from bs4 import BeautifulSoup

html = """
<div class="content">
E-Mail：<a href="mailto:mail@test.com.tw">mail</a><br>
E-Mail2：<a href="mailto:mail2@test.com.tw">mail2</a><br>
<ul class="price">定價：360 元 </ul>
<img src="http://test.com.tw/p1.jpg">
<img src="http://test.com.tw/p2.jpg">
<img src="http://test.com.tw/p3.png">
</div>
"""

soup = BeautifulSoup(html, 'html.parser')
data = soup.select('.price')[0].text # .select css選擇器
print(data)

# 用正則表達式抓取特定內容
print(re.findall('([0-9]+)', data)[0]) # 只抓數值，便於寫進資料庫

emails = re.findall(r'[a-zA-Z0-9_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9_.]+', html)
for email in emails:
    print(email)
      