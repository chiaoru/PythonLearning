# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 21:06:58 2023

@author: USER
"""

from bs4 import BeautifulSoup

html_doc = """
<html><head><title>Hello World</title></head>
<body><h2>Test Header</h2>
<p>This is a test.</p>
<a id="link1" href="/my_link1">Link 1</a>
<a id="link2" href="/my_link2">Link 2</a>
<p>Hello, <b class="boldtext">Bold Text</b></p>
<img src="iu.jpg">

<div id="area">
<p>This is a test.</p>
<a id="link1" href="/my_link1">Link 1</a>
<a id="link2" href="/my_link2">Link 2</a>
<p>Hello, <b class="boldtext">Bold Text</b></p>
<img src="iu.jpg">
</div>

</body></html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')
#print(soup.prettify()) # 排版格式化

title = soup.find('title')
h2 = soup.find('h2')
p = soup.find('p')
p2 = soup.find_all('p')

print(title)
print(h2)
print(p)
print(p2)

print()

# 只印出標籤內的內容
title = soup.find('title').text
h2 = soup.find('h2')
p = soup.find_all('p')

print(title)
print(h2.text)

a = soup.find('a')
print(a)

link = a.get('href')
txt = a.text
print(link)
print(txt)

img = soup.find('img').get('src')
print(img)

a_id = soup.find(id='link2')
print(a_id)

print()

textarea = soup.find(id='area')
print(textarea)
print()
tp = textarea.find('p').text
print(tp)





