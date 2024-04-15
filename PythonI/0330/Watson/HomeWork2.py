# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 19:19:57 2023

@author: USER
"""

num = list()
while len(num) < 6:
    n = int(input('pls input number:'))
    if num.count(n) == 0:
        num.append(n)
    else:
        print(n,"Ya")
        
     
print(num)    

leng = len(num) #6

for i in range(leng - 1): # range(5) => 0,1,2,3,4)
    for x in range(leng - i - 1): #6-0-1  , 6-1-1,6-2-1
        if num[x] < num[x+1]:
            num[x],num[x+1] = num[x+1],num[x]
print(num)            
    
    