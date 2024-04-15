# -*- coding: utf-8 -*-
"""
Created on Thu May  4 19:40:37 2023

@author: USER
"""

fn = 'file02.txt'

with open(fn, encoding='utf-8') as fobj:
    #data = fobj.readline() #只讀取單行
    datas = fobj.readlines() # 每次讀取一行，並存入串列 list 中
print(datas)

for line in datas:
    print(line.strip()) #strip() 去除前後空白
    
print(datas[2]) # 因為是串列，所以也可以指定想要的內容

