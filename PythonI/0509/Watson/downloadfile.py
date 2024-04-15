# -*- coding: utf-8 -*-
"""
Created on Tue May  9 19:23:38 2023

@author: USER
"""



import requests


url  = "https://uc.udn.com.tw/photo/2023/05/06/0/21869396.jpg"

data = requests.get(url,stream=True)

with open('lcc.jpg','wb') as f:
    for block in data.iter_content(1024):
        if not block:
            break
        f.write(block)
