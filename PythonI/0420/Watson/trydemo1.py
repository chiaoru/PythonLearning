# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

data = [100,80,60,70]

try:
    
    ans = 100 / 0 
    
    print(data[0])
    print(data[2])
    print(data[10])
    print(data[1])
    
except (IndexError,ZeroDivisionError) as ex:
    
    print(ex)    

print("程式執行完畢")