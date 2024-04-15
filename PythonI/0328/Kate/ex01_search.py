# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 19:29:35 2023

@author: USER
"""

scores = [60,70,65,100,91,88,65,81]

search = 65
start = 0 # 設定index的起始值

for i in range(scores.count(search)):
    index = scores.index(search,start) # 設定index的起始值，當跑迴圈時才能接續往下一個找
    print("索引值：",index)
    start = index + 1 #才能接續往下找，否則會一直在同一個索引值搜尋即跳出