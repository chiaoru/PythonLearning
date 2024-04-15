#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 17:33:46 2023

@author: kate
"""

def showList(datalist, num):
    try:
        print(datalist[num])
    except IndexError as e:
        print("超出範圍")
        #pass # 如有發生問題會被略過
        raise IndexError("請處理索引值超出")
        
data = [10, 20, 30]

try:
    showList(data, 1)
    showList(data, 5)
except Exception as e:
    print("Error:", e)

print("程式執行完畢！")