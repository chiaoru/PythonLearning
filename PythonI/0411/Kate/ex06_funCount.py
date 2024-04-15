# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 20:53:53 2023

@author: USER
"""

# 函式計算
def total(n1, n2, n3):
    res = 0
    for i in range(n1, n2+1, n3): # 因為 n2 也要計算，所以n2+1
        res += i
    return res

print("計算總和")

key = input("按 y 開始:")
key.lower()

while key == 'y':
    start = int(input("請輸入初始值:"))
    end = int(input("請輸入終止值:"))
    sep = int(input("請輸入間隔值:"))
    result = total(start, end, sep)
    print("總和:", result)
    key = int(input("按 y 繼續:"))
    

