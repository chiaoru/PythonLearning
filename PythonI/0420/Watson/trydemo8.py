# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 20:21:33 2023

@author: USER
"""


def divResult(num1,num2):
    
    if num2 == 0 :
        raise ZeroDivisionError("不可以為0")
    
    try:
        result = num1 // num2
        print("結果：",result)
    except Exception as e:
        print(e)
    finally:
        print('不管是否有引發錯誤，都會執行')
    
        
    
try:    
    divResult(100,20)
    divResult(100,0)    
except Exception as e:
    print(e)    
print('程式執行完畢')