# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 21:05:10 2023

@author: USER
"""

def total(n1,n2,n3):
    res = 0
    for i in range(n1,n2+1,n3):
        res += i
        
    return res


print('計算總和')
key = input('按y開始')

while key == 'y':
    start = int(input())
    end = int(input())
    step = int(input())
    result = total(start,end,step)
    print("總和：",result)
    key = input('按y繼續')    