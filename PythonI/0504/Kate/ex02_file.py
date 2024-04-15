# -*- coding: utf-8 -*-
"""
Created on Thu May  4 19:12:53 2023

@author: USER
"""

fn = 'file01.txt'
fobj = open(fn) # 預設是 r fobj = open(fn, 'r')
data = fobj.read()
fobj.close()
print(data)


fn2 = 'file02.txt'
fobj2 = open(fn2, encoding='utf-8') # encoding 編碼，中文需編碼，否則出錯
data = fobj2.read()
fobj2.close()
print(data)
