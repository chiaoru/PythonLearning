# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Father:
    
    def car(self):
        print("Father Car")
        
    def house(self):
        print("Father House")
        
        
class Son(Father):
    def school(self):
        print('Son的學校：聯成分校')
   


s = Son()

s.car() 
s.house()       
s.school()

s2 = Son()
s2.car() 
s2.house()       
s2.school()



