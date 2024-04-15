# -*- coding: utf-8 -*-
"""
Created on Tue May  2 19:08:11 2023

@author: USER
"""

class Father:
    
    def car(self):
        print("Father Car")
        
    def house(self):
        print("Father House")
        
        
class Mother():
    def car(self):
        print('Mother Car')

    def Clothes(self):
        print('漂亮的衣服')
        
        
#繼承順序有先後        
class Son(Father,Mother):
    def school(self):
        print('Son的學校：聯成分校')
        
        
s = Son()

s.Clothes()
s.car()
s.house()
s.school()        
        
        
        
        
        
        
        
        