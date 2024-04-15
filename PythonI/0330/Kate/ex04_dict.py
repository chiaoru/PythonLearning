# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 21:22:00 2023

@author: USER
"""

content = {"A":"內向","B":"樂觀","O":"自信","AB":"負責"}

blood = input("請輸入血型:")
blood = blood.upper() # 將輸入值轉成大寫
# blood = blood.lower() # 將輸入值轉成小寫

if content.get(blood) == None:
    print("找不到血型:",blood)
else:
    print("血型:", blood, content[blood])
