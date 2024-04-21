# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 21:30:54 2023

@author: USER
"""

# 多重繼承
class Grandfather:
    def action(self):
        print('Grandfather')
        
class Grandmother:
    def action(self):
        print('Grandmother')
        
class Father(Grandfather):
    def action2(self):
        print('Father')
        
class Uncle(Grandmother):
    def action(self):
        print('Uncle')
        
class Child(Father, Uncle):
    def action3(self):
        print('Child')
        
        
John = Child()
John.action3()
John.action2()
John.action()