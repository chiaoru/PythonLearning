# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 21:00:24 2023

@author: USER
"""

# homework 2
for i in range(1,10,2):
    print("|"*i)
    
# homework 2-1
for i in range(4,-1,-1):
    print(" "*i,"|"*(9-i*2))



# homework 2-3
for i in range(5,0,-1):
    print(str(i)*i)
    if int(i) == 1:
        for i in range(2,6):
            print(str(i)*i)
    
