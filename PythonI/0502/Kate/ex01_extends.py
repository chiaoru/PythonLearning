# -*- coding: utf-8 -*-
"""
Created on Tue May  2 18:42:09 2023

@author: USER
"""

class Father:
    def car(self):
        print('Father Car')
    
    def house(self):
        print('Father House')
        
class Son(Father): # 繼承 class Father中的東西
    #pass # 暫時不寫東西
    
    def school(self):
        print('Son 的學校: 聯成分校')
        
    
    
s = Son()

s.car()
s.house()
s.school()

s2 = Son()

#s2 與 s 為兩個不同物件，互不影響

s2.car() 
s2.house()
s2.school()
