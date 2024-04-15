#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 21:53:09 2023

@author: kate
"""

"""

homework 3
    1. 由使用者輸入3個值(整數)，判斷是否可構成三角形
        (任兩邊何必大於第三邊)
    2. 判斷是否為等腰三形或正三角形

"""



a = int(input("請輸入三角形第一邊長："))
b = int(input("請輸入三角形第二邊長："))
c = int(input("請輸入三角形第三邊長："))


# 3-1
if (a+b) > c and (a+c) > b and (b+c) > a:
    print("三角形成立！")
else:
    print("三角形不成立！")
    
print()
    
# 3-2
if (a+b) > c and (a+c) > b and (b+c) > a:
    print("三角形成立！")
    if a == b and  b == c:
        print("是正三角形！")
    elif a==b or b == c:
        print("是等腰三角形！")
    else:
        print("是不等邊三角形！")
else:
    print("三角形不成立！")