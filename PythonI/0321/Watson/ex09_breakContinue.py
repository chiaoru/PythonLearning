# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 21:38:31 2023

@author: USER
"""

for i in range(1,10):
    for y in range(2,10):
        if i*y >= 18:
            break #離開當下的迴圈，而非全部的迴圈
        print(i, "X", y, "=", i*y, sep="", end="\t")
print("程式執行完畢!")