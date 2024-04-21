# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 20:03:57 2023

@author: USER
"""


class ObjectDemo:
    # 建構值(一般不會寫，會自動生成)
    def __new__(cls): # 本身還沒有物件產生
        print('__new__')
        return object.__new__(cls) # 產生一個物件
    
    def __init__(self):
        print('__init__')
        
        
obj = ObjectDemo()


class ObjectDemo2:
    def __new__(cls):
        print('__new__')
        return None # 如未生成物件，即不能生成self
    
    def __init__(self):
        print('__init__')
        
    def go(self):
        self.name = 'Bill'
        print(self.name)
        
obj2 = ObjectDemo2()
obj2.go()