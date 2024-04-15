# -*- coding: utf-8 -*-
"""
Created on Tue May  9 20:51:24 2023

@author: USER
"""

import random

numbers = list()

n = int(input('請輸入組數：'))

for i in range(n):
    num = list()
    while len(num) < 6:
        ran = random.randint(1,49)
        if num.count(ran) == 0:
            num.append(ran)
    numbers.append(num)        
    
print(numbers)    

# 開獎
result = list()
while len(result) < 6:
    ran = random.randint(1,49)
    if result.count(ran) == 0:
        result.append(ran)

print("開獎：",result)  

print("對獎開始了....")      

for row in numbers:
    point = 0
    for n in row:
        if result.count(n) == 1:
            point += 1
            
    print(row,'中了',point,'個')


        
        
        

