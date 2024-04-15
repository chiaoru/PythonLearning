#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 17:30:36 2023

@author: kate
"""

def divResult(num1, num2):
    
    if num2 == 0: # 手動檢查自己的錯誤
        raise ZeroDivisionError("不可以為0")  # 當出現錯誤時跳出
        
    try:
        result = num1 / num2
        print("結果：", result)
        
    except Exception as e:
        print(e)
        
    finally:
        print("計算完畢") # 不管有沒有錯誤都一定會執行
        print("不管是否有引發錯誤，都會執行")

# callStack 當有問題時會傳給呼叫者
try: # 如不確定別人的函式是否有寫例外處理時，可自行補上
    divResult(100,20)
    divResult(100,0)

except Exception as e:
    print(e)
    

print("程式執行完畢！") # 不會被執行，因為例外未處理