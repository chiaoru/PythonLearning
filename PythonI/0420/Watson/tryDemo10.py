# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 21:33:17 2023

@author: USER
"""

def plusNumber(n1,n2):
    try:
        result = n1 // n2
    except Exception as e:
        print(e)
        
    else:
        print('計算結果：',result)
        print('程式執行完畢')
        
        
plusNumber(10,2)
plusNumber(10,0)        
        