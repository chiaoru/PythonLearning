# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 20:23:10 2023

@author: USER
"""

data = (10,20,30,40)
print(type(data))

print(data[0])

#data[0] = 100

listdata = list(data)

listdata[0] = 100

data = tuple(listdata)

print(data)

print()

number = 1,2,3,4,5

print(number)