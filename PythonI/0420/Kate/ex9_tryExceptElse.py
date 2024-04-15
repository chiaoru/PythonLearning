#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 18:02:26 2023

@author: kate
"""

def plusNumber(num1, num2):
    try:
        result = num1 // num2
    
    except Exception as e:
        print(e)
        
    else: # 當條件不成立會跑這裡
        print('計算結果：', result)
        print('程式執行完畢')
    
    
plusNumber(10, 2)
plusNumber(10, 0)