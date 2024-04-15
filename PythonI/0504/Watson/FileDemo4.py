# -*- coding: utf-8 -*-
"""
Created on Thu May  4 19:49:37 2023

@author: USER
"""

fn = "file03.txt"

msg = "Python 是一個超好學的程式語言"

data = ['聯成','電腦','python','100']

with open(fn,'w',encoding='utf-8') as f:
    
    f.write(msg + '\n')
    
    for line in data:
        f.write(line + '\n')
        
        