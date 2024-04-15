# -*- coding: utf-8 -*-
"""
Created on Tue May  2 20:38:17 2023

@author: USER
"""

class A:
    def aMethod(self):
        print('aMethod')
        
class B(A):
    def bMethod(self):
        print('bMethod')
        
    def display(self):
        print('b-display')
        
class C(B):
    def cMethod(self):
        print('cMethod')
        
    def display(self):
        print('c-display')
        
class D(C, B):
    def dMethod(self):
        print('dMethod')
        
        
a = C()
a.aMethod() # B繼承A
a.bMethod() 
a.display() # 自己有先用自己的


d = D()
d.display() # c-display，因為當繼承C,B時，先找到c中的display
