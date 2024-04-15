# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 19:12:14 2023

@author: USER
"""

print(list(range(10)))
print(list(range(1,10)))
print(list(range(2,10,2)))


total = 0
for i in range(10): # for 迴圈用於次數已知
    print(i)
    total += i # 累加
print("總和：",total)

t = 0
for i in range(5,50,5):
    t += i
    print(t)
print("總和:",t)

num = int(input("請輸入次數:"))
total = 0
for i in range(num): 
    print(i)
    total += i 
print("總和：",total)


num = int(input("請輸入階層:"))
total = 1
for i in range(1,num+1): 
    print(i)
    total *= i # 累乘
print("總和：",total)


    
    
    
    
    
