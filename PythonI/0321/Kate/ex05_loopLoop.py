# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 20:00:26 2023

@author: USER
"""

for i in range(1,5): #[1,2,3,4]
    print("i=", i) 
    for y in range(3): #[0,1,2]
        print(y, end=",")
    print()
print("程式執行完畢!")


# 九九乘法表
for i in range(1,10):
    for j in range(1,9):
        print(i, "X", j, "=", i*j, sep=" ", end="\t")
        
        
print("*"*15)

for a in range(2,10):
    for b in range(1,10):
        print(a, "*", b, "=", a*b, sep="", end="\t")
    print()

print()

# 換排版方式    
for a in range(2,10):
    for b in range(2,10):
        print(b, "*", a, "=", a*b, sep="", end="\t")
    print()