# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 19:40:17 2023

@author: USER
"""


data = [100,80,60,70]


try:

    print(data[0])
    print(data[2])
    print(data[10])
    print(data[1])
    print(data(1))
    ans = 100 / 0 
    
except IndexError as ex:    
    print("索引值超過")    
except:
    print("其他的Error")    

print("程式執行完畢")