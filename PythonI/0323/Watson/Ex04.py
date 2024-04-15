# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 20:57:45 2023

@author: USER
"""

scores = list()
while True:
    number = int(input("請輸入分數-1離開："))
    if number == -1:
        break
    
    scores.append(number)
    
    
print(scores)    
    