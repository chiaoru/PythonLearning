# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 19:16:44 2023

@author: USER
"""

def sayHello():
    print("Hello")
    print("哈囉！！")
    print("你好！！！")
    
    
start = 99    
    
def runfor(start,end,sep):
    
    # 在函式中，所定義的變數名稱 都是 區域 變數 (除非有特別指定)
    a = 10
    for i in range(start,end,sep):
        print(i)
    
    
    
    
    
sayHello()    

runfor(5,15,3) # 位置參數


print(start)

  