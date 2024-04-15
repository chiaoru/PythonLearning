# -*- coding: utf-8 -*-
"""
Created on Thu May  4 19:49:58 2023

@author: USER
"""

# 寫入檔案

fn = 'file03.txt'

msg = 'Python 是一個超好學的程式語言'

data = ['聯成', '電腦', 'Python']

with open(fn, 'w', encoding='utf-8') as f: # 'w' 為覆寫，每次開啟檔案都會清掉，然後寫入的東西覆蓋
    for line in data:
        f.write(line + '\n')
        
    f.write(msg + '\n') # 斷行寫入