# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


scores = [100,99,80,70,89,66,50,70,70]

while True:
    num = int(input("pls delete number -1 exit:"))
    if num == -1:
        break
    
    if scores.count(num) > 0 :
        start = 0
        for i in range(scores.count(num)):
        
            index = scores.index(num,start)
            scores.pop(index)
            start = index
            
        print("List data:",scores)
        
    else:
        print("Not found")
    
    








