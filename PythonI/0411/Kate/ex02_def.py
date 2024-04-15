# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 19:20:45 2023

@author: USER
"""

def sayHello(): # 無參數函式
    print("Hello!")
    print("Ola!")
    print("Bonjour!")
    print("你好!")
    print()
    
sayHello() # 呼叫無參數自訂函式

start = 99

def runfor(start,end,sep): # 有參數函式
    # 在函式中，所定義的變數名稱都是區域變數(除非有特別指定)
    for i in range(start,end,sep):
        print(i)
        
runfor(5,15,2) # 呼叫有參數自訂函式(位置函式)

print(start) # 答案是99，因為在區域外