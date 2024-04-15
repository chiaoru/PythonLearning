# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 19:53:04 2023

@author: USER
"""


def bigValue(x,y):
    if x > y:
        return x
    else:
        return y
   
    
x = int(input("輸入X:"))   
y = int(input("輸入y:"))
    
big = bigValue(x,y)
print("最大值：" , big)   
    

def circle(r):
    area = r * r * 3.14
    per = 2 * r * 3.14
    
    return area,per

ci = circle(5)
area,p = circle(12)

print(ci)
print()
print(area)
print(p)



