# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 20:55:37 2023

@author: USER
"""

import random # 崁入亂數函數庫

print(random.random()) # 範圍是0~1的浮點數，最小不會是0，最大不會是1

ans = random.randint(1,100) #由系統隨機取數1~100之間的值

#ans = 91
guess = 0

while guess != ans:
    guess = int(input("請輸入1~100之間猜數:"))
    if guess > ans:
        print("猜小一點!")
    elif guess < ans:
        print("猜大一點!")
    else:
        print("猜對了!")
        
        
"""
break 跳離當下的迴圈

continue 這一次放棄不做，跳下一個


"""
    