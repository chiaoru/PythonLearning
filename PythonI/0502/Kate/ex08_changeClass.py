# -*- coding: utf-8 -*-
"""
Created on Tue May  2 21:31:49 2023

@author: USER
"""

# 動態變更類別(只有python 可以)
class Father:
    def display(self, name):
        self.name = name
        print('Father name is:', self.name)
        
class Mother:
    def display(self, name):
        self.name = name
        print('Mother name is:', self.name)
        
        
class Child(Father, Mother):
    pass

class Son(Father):
    pass


print(Child.__name__, '繼承')

for item in Child.__bases__: #印出動態繼承類別有哪些
    print(item)
    
print(Son.__name__, '繼承')
print(Son.__bases__) # (<class '__main__.Father'>,)

son = Son()
son.display('David') # 印出 Father.display

Son.__bases__ = (Mother,) # 改變類別(動態)
son.display('Mary') # 印出 Mother.display