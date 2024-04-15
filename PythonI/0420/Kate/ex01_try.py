#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 10:45:35 2023

@author: kate
"""

# 例外處理

data = [100, 80, 50, 70]

try:
    ans = 100/0
    
    print(data[0])
    print(data[2])
    print(data[10]) # 如未作例外處理，會出現 ist index out of range，所以用try except來抓出錯誤並讓程式順利執行
    print(data[1]) # 不會被執行，因為except 執行完會往下走
    
    
except (IndexError, ZeroDivisionError) as ex: # 選擇需要抓出的例外
    
    print(ex)
    #print("抓到超過索引範圍")
    
print("程式執行完畢！")

# leet code 可以練習解程式