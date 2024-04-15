# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 21:18:53 2023

@author: USER
"""

''''
if 布林判斷式(條件式):
   成立時要執行的程式區段 
   
print() -->在程式區塊外，屬於另一個區塊
   

通常程式區塊縮排為一個tab鍵，也可是固定空白鍵，但必須統一，否則會出錯
'''

age = 26
if age >= 18: # 當條件成立才執行
    print("可以考駕照!")
    print("可以買菸酒!")
    print("可以投票!")
    
print("程式執行完畢!")

scores = 59
if scores >= 60:
    print("及格!")
else:
    print("不及格!")
print("程式執行完畢!")