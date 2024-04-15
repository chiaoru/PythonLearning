# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 21:03:22 2023

@author: USER
"""

import random  # 嵌入亂數函式庫
print(random.random()) # 範圍是0~1之間的浮點數，最小不會是0 ，最大不會是1

ans = random.randint(1,100) # 由系統隨機取數1~100之間的值
guess = 0

while guess != ans :
    guess = int(input("請輸入1~100之間的整數："))
    if guess > ans:
        print("請猜小一點")
    elif guess < ans:
        print("請猜大一點")
        
print("猜對了")        