# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 20:08:34 2023

@author: USER
"""

def divResult(num1,num2):
    try:
        result = num1 // num2
        print("結果：",result)
    finally:
        print('不管是否有引發錯誤，都會執行')
    
        
divResult(100,20)
divResult(100,0)    
print('程式執行完畢')