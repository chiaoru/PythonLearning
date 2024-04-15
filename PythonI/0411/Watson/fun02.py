# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 19:35:15 2023

@author: USER
"""

money = 199

def interest(rate):
    global money
    money = 100000
    inter = money * rate
    print("利息：",inter,'元')
    
 
    
    
interest(0.06)    

print(money)

    

