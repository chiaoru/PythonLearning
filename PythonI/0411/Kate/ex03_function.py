# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 19:35:54 2023

@author: USER
"""

money = 199

def interest(rate):
    global money # 當未設定此 全域變數global 時，函式內外的相同名稱變數互不影響
    money = 100000 
    inter = money * rate
    print("利息為:", inter)
    
interest(0.06)

print(money) # 因函式內的全域變數關係，所以函式外的變數也被更改

# 可回傳值 return 與不可回傳值

print(interest(0.01)) # --> 答案是 None，因為函式內沒有回傳值 return