# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 18:43:16 2023

@author: USER
"""

n = int(input("欲顯示幾層的巴斯卡三角形:"))

data = [1]

for i in range(n):
    print(data)
    plist= []
    plist.append(data[0]) # 變二為串列
    for i in range(len(data)-1):
        plist.append(data[i]+data[i+1])
    plist.append(data[-1])
    data = plist