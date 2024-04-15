#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 12:41:49 2023

@author: kate
"""

import random


# 猜終極密碼，提示給予範圍
lowest = 1

highest = 100

ans = random.randint(lowest, highest)

count = 0

guess = 0

while guess != ans:

    if count < 5:
        guess = int(input("請輸入1~100之間猜數："))
        count += 1
        
        if guess > ans:
            highest = guess
            print("猜小一點！密碼介於 ", lowest, "~", highest,"之間")
            
        elif guess < ans:
            lowest = guess
            print("猜大一點！密碼介於 ", lowest, "~", highest,"之間")
        else:
            print("猜對了！")
            break
        print()
                
    else:
        print("猜錯五次，答案是：", ans)
        break


