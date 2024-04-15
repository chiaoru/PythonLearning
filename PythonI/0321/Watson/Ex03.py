# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 19:21:55 2023

@author: USER
"""

print(list(range(10)))
print(list(range(1,10)))
print(list(range(2,10,2)))


num = int(input("輸入次數："))

total = 0
for i in range(num):
    print(i)
    total += i
    
print("總和：",total)    
    

num = int(input("輸入階層："))

total = 1
for i in range(1,num+1):
    print(i)
    total *= i
    
print("總和：",total)    