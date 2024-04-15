# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 19:02:43 2023

@author: USER
"""

acc = input("輸入帳號：")
pwd = input("輸入密碼：")

if acc == "lcc" and pwd == "123456":
    print(acc, "歡迎回來!")
    print("登入成功!")
else:
    print("帳密錯誤，登入失敗!")
    
    