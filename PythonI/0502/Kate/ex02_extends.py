# -*- coding: utf-8 -*-
"""
Created on Tue May  2 19:08:43 2023

@author: USER
"""

class Father:
    def car(self):
        print('Father Car')
    
    def house(self):
        print('Father House')
        
class Mother:
    def car(self):
        print('Mother Car')
        
    def Clothes(self):
        print('漂亮的衣服')
   
# 繼承順序有先後，先找自己有的，再找爸爸有的，最後找媽媽
class Son(Father, Mother): # 如果媽媽寫前面，就會先找媽媽的物件，沒有再找爸爸的
    
    def school(self):
        print('Son 的學校: 聯成分校')
        
s = Son()

s.Clothes() # 繼承媽媽
s.car() # 繼承爸爸
s.house() # 繼承爸爸
s.school() # 自己有的
