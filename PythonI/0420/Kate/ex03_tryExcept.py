#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 16:52:51 2023

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
except IndexError as ex: # 選擇需要抓出的例外
    
    print("索引值超過")
    #print("抓到超過索引範圍")
    
except:
    print("其他的Error")
    
print("程式執行完畢！")