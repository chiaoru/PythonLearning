# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 21:09:28 2023

@author: USER
"""

import re
from bs4 import BeautifulSoup

soup = BeautifulSoup('<p class="body strikout">Test</p>', 'html.parser')
p = soup.find('p', class_='strikout').text

p_tag = soup.select('p.body.strikout')[0].text

print(p)
print(p_tag)

soup = BeautifulSoup('<p id="news">新聞</p>', 'html.parser')

news = soup.find(id='news').text

cssNews = soup.select('#news')[0].text

print(news)
print(cssNews)