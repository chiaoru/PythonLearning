# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 19:07:48 2023

@author: USER
"""

acc = input("請輸入帳號：")
pwd = input()

if acc == "lcc" and pwd == "123456":
    print("登入成功")
    print(acc,"歡迎回來")
else:
    print("帳密錯誤")    