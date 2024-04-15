# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 18:48:46 2023

@author: USER
"""

def displayScore(**score): # **用字典方式帶入
    print("成績:", score)
    
displayScore(eng=72,  python=81, math=99)

def showScore(name, **score):
    print("Name:", name)
    print("Grade:", score)

print()    
showScore("Bill", eng=70, python=90, math=60)
    
    