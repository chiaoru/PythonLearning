# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 19:47:38 2023

@author: USER
"""

# 串列
scores = [100,96,98,80,100] # 一般放同性質的值
items = [99,"一中",3.14,True] # 只有python 可以放不同性質的值

# 串列中的抓法
print(items[1])
print(scores[0])


number = [1,2,3,4,5,6,7,8,9,0]
print(number[-1])  # 只有python 可以這樣做
print(number[-2])
print(number[2:5]) # 從索引值2開始抓到5之前，不含5
print(number[:5]) # 從索引值0開始抓到5之前，不含5
print(number[5:])  # 從索引值5開始抓到結束
print(number[1:9:2]) # 從索引值1開始抓到9之前，不含9，間隔2
print(number[-1:]) # 從索引值倒數第一個開始抓到結束
print(number[-1::-1]) # 從索引值倒數第一個開始抓到

#將值依序抓出
for i in range(len(number)): # len 計算長度；range(len(number) 是串列，所以可以直接用number取代
    print(number[i])

print()

# 因為number是串列，所以用迴圈方式將個別值印出
for it in number:
    print(it)