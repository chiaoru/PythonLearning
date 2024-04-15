# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def displayScore(**score):
    print(score)
    
    
def showScore(name,**score):
    print("Name:",name)
    print(score)
    
    
displayScore(eng=77,python=81,math=99)

print()
showScore("Bill",eng=77,python=81,math=99)    