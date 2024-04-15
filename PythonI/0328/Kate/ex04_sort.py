# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 20:31:18 2023

@author: USER
"""
#sort 在原本串列中排序
number = [99,66,33,45,65,89,80]

number.sort() # 預設為小到大
print(number)

number.sort(reverse=True)
print(number)
print()

#sorted # 創一個新串列來排序
number = [99,66,33,45,65,89,80]
newNum = sorted(number)
print(newNum)
print(number)
print()

newNum2 = sorted(number, reverse= True)
print(newNum2)
print(number)