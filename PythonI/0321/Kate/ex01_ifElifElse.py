# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 18:50:30 2023

@author: USER
"""

# score = 490
score = int(input("輸入分數："))

if score >= 600:
    print("優")
elif score >= 500:
    print("甲")
elif score >= 400:
    print("乙")
else:
    print("丙")
print("程式執行完畢")