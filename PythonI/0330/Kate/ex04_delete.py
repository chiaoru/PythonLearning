# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 21:37:53 2023

@author: USER
"""

# 刪除 delete -> del

fruit = {"apple":34, "orange":68, "banana":49}

fruit["orange"] = 168
print(fruit)

del fruit["apple"] # delete
print(fruit)

fruit.clear() #全清
print(fruit)