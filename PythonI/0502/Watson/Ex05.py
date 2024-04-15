# -*- coding: utf-8 -*-
"""
Created on Tue May  2 20:49:45 2023

@author: USER
"""



class A:
    def aMethod(self):
        print('aMethod')
        
        
class B(A):        
    def bMethod(self):
        print('bMethod')
    def display(self):
        print('B-Display')
        
class C(B):        
    def cMethod(self):
        print('cMethod')        
        
    def display(self):
        print('C-display')
        
class D(C,B):
    def dMethod(self):
        print('D-Method')
        
        
        
a = C()
a.cMethod()
a.bMethod()
a.aMethod()
a.display()        


d = D()
d.display()


