#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 22:25:34 2023

@author: kate
"""

import random

ans = random.randint(1, 100)

guess = 0

count = 0

# 猜數，限制次數
while guess != ans:
    count += 1
    if count < 6:
        guess = int(input("請輸入1~100之間猜數："))
        if guess > ans:
            print("猜小一點！")
        elif guess < ans:
            print("猜大一點！")
        else:
            print("猜對了！")
    else:
        print("猜錯五次，答案是：", ans)
        break


