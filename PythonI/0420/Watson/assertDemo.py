# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 21:11:56 2023

@author: USER
"""


def score(number):
    
    if number < 0 :
        return '不可以小於0'
    else:
    
    
        #斷言  預設都是 True ，若斷言失敗時，就要修正
        assert number >= 0 , '輸入值要大於0'
        
        print('分數：',number)
    
print(score(-60))
    
    
    
    