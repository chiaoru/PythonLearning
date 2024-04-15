# -*- coding: utf-8 -*-
"""
Created on Thu May  4 20:03:14 2023

@author: USER
"""

fn = 'file04.txt'

msg = 'Python 是一個超好學的程式語言'

data = ['聯成', '電腦', 'Python', '100']

with open(fn, 'a', encoding='utf-8') as f: # 'a' 為續寫，會接續檔案內的內容往下寫
    for line in data:
        f.write(line + '\n') # 寫入資料必須為字串
        
    f.write(msg + '\n') # 斷行寫入