# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 20:39:46 2023

@author: USER
"""

fruits = {"香蕉":69,"蘋果":45,"香瓜":100}

price = fruits.setdefault("香蕉")
print(price)

price = fruits.setdefault("香蕉",110)
print(price)

price = fruits.setdefault("芭樂",70)
print(price)

price = fruits.setdefault("黃金果")
print(price)

print(fruits)

