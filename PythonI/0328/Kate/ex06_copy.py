# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 21:21:49 2023

@author: USER
"""

# 淺複製 copy

import copy # 複製函式

data = [100,200,300,400]
num = copy.copy(data) # 潛複製，用於一維串列 copy.copy(iterator) iterator 一般是串列

data.append(10)
print(num) # 內容不會被複製影響
print(data) 

# 深複製 deep copy
data2 = [[10,20,30],[1,2,3,4,5,6]] # 二維串列(多維串列)，從最外面往內抓
print(data2[1])
print(data2[0][2])
print(data2p[1][4])