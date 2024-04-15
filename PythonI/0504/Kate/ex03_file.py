# -*- coding: utf-8 -*-
"""
Created on Thu May  4 19:26:34 2023

@author: USER
"""

fn = 'file02.txt'

with open(fn, encoding='utf-8') as fobj:
    # with open 會自行執行關閉(finally 必須執行的動作)
    #data = fobj.read()
    
    # 逐行印出
    for line in fobj:
        print(line)
        print('-'*30)
    
#print(data)
    