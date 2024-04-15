#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 16:58:03 2023

@author: kate
"""

data = [100, 80, 50, 70]

try:
    
    print(data(1)) # typeError
    ans = 100/0
    
    print(data[0])
    print(data[2])
    print(data[10]) # 如未作例外處理，會出現 ist index out of range，所以用try except來抓出錯誤並讓程式順利執行
    print(data[1]) # 不會被執行，因為except 執行完會往下走
    


# 兩個例外要分開處理
except Exception as ex:
    print(ex)
    
print("程式執行完畢！")

def divResult(num1, num2):
    try:
        result = num1 / num2
        print("結果：", result)
    except Exception as e:
        print("錯誤：", e)
    finally:
        print("計算完畢") # 不管有沒有錯誤都一定會執行
        print("不管是否有引發錯誤，都會執行")
        
divResult(100,20)
divResult(100,0)

print("程式執行完畢！") # 會被執行