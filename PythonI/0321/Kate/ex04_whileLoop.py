# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 19:46:03 2023

@author: USER
"""

# while 迴圈用於次數未知 

i = 1
while i < 10: # 條件符合才會進入迴圈
    print(i)
    i += 1 # 才不會造成無窮迴圈
print("程式執行完畢!")

for i in range(10, 0, -1):
    print(i)
    
i = 10
while i >= 1:
    print(i)
    i -= 1
    
