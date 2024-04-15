# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 19:54:18 2023

@author: USER
"""

def bigValue(x,y):
    if x > y:
        return x
    else:
        return y
    
x = int(input("請輸入 x 的值:"))
y = int(input("請輸入 y 的值:"))

big = bigValue(x, y)

print("最大值:", big)


# 函式呼叫
def circle(r):
    area = r**2*3.14
    per = 2*r*3.14
    return area, per

ci = circle(5)
area, p = circle(12)

print(ci)
print(area)
print(p)
    