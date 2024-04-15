# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 20:33:00 2023

@author: USER
"""

# 設定預設值 setdefault

fruits = {"Banana":66, "Apple": 45, "Melon":100}

price = fruits.setdefault("Banana")
print(price)
price = fruits.setdefault("Banana",110) 
# 如果字典內的key如果有value,則不能把值110給予key(Banana),如果沒有，則把值給予key
print(price)

price = fruits.setdefault("Grava", 70)
print(price)
price = fruits.setdefault("Abiu") #黃金果
print(price)
print(fruits)