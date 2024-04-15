# -*- coding: utf-8 -*-
"""
Created on Thu May  4 21:28:24 2023

@author: USER
"""

fn = 'file02.txt'

with open(fn, encoding='utf-8') as f:
    data = f.read()
    newdata = data.replace('重啟', 'close')
    print(newdata.strip())
    
with open('news.txt', 'w', encoding='utf-8') as f:
    f.write(newdata.strip())