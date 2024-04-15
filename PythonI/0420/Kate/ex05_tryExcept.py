#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 17:13:46 2023

@author: kate
"""

# try 可單獨搭配finally或except，也可三者一起，但不能單獨使用
def divResult(num1, num2):
    try:
        result = num1 / num2
        print("結果：", result)
        
    finally:
        print("計算完畢") # 不管有沒有錯誤都一定會執行
        print("不管是否有引發錯誤，都會執行")


divResult(100,20)
divResult(100,0)

print("程式執行完畢！") # 不會被執行，因為例外未處理