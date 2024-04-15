# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 20:18:08 2023

@author: USER
"""

# 元組，只能讀，不能改

data = (10,20,30,40)
print(type(data))
print(data)
print(data[0])

#data[0] = 100 # Error，因為元組無法被改變
# 當要改變，只能先轉成串列之後再改回元組
listdata = list(data)
listdata[0] = 100
data = tuple(listdata)
print(data)

number = 1,2,3,4,5 # 預設資料型態為元組
print(number)
print(type(number))