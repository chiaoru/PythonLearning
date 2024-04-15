# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class myBirth:
    def __init__(self,name,y,m,d):
        self.name = name
        self.year = y
        self.month = m
        self.day = d
        
    #重新定義方法
    #定義輸出的格式    
    def __str__(self):
        print(self.name,'你好')
        return '生日：'+str(self.year)+'年'
        
    def __repr__(self):
        return '生日{}年{}月{}日'.format(self.year,self.month,self.day)


birth = myBirth('Bill',1999,9,21)
print(birth)       

print(repr(birth))


 