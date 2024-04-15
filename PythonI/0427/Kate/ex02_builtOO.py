# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 21:40:14 2023

@author: USER
"""

class myClass:
    
    # 建構物件
    def __new__(Kind, name):
        if name != '':
            print('建立物件!')
            return object.__new__(Kind)
        
        else:
            print('未建構物件!')
            return None
                
    def __init__(self, name):
        print('物件初始化')
        print(name)
        
x = myClass('')
print()

y = myClass('Bill')