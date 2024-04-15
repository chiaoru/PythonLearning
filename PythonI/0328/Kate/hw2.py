# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 20:45:49 2023

@author: USER
"""

"""
homework 2
2-1. 由使用者分別輸入六個數字，並放入串列中，請用巢狀迴圈進行由大至小排序，並印出結果。
2-2. 如果使用者輸入的數字一樣的話，則不加入，請使用者重新輸入。

"""

number = []

for i in range(6):
    
    a = int(input("請輸入第{}個數字：".format(i+1)))
    if number.count(a) > 0:
        print("已有相同的數字，請重新輸入！")
        a = int(input("請輸入第{}個數字：".format(i+1)))
        number.append(a)
        print(number)
        
    else:    
        number.append(a)
        print(number)

print("排序前為",number)

# 氣泡排序演算法
for a in range(len(number)-1):
    #print(number[a], sep=" ", end=" ")

    for b in range(len(number)-a-1):
        #print(number[b], sep=" ", end=" ")
        if number[b] < number[b+1]:
            number[b], number[b+1] = number[b+1], number[b]
            
print("排序後為：",number)

# ans

num = list()

while len(num) < 6:
    n = int(input("請輸入數字:"))
    if num.count(n) == 0:
        num.append(n)
    else:
        print(n,"重複")
        
print("排序前:",num)
 
 # 氣泡排序法, 兩兩相比

length = len(num)

for i in range(length-1): # 兩兩相比，不用全部比完
    for x in range(length-i-1): # 讓範圍越來越小，因為最大/最小已經比過了，所以就不用再比了
        if num[x] < num[x+1]: # 排序大到小
            num[x], num[x+1] = num[x+1], num[x] # 只有python 可以這樣寫
print("排序後:", num)
            
        
    

        
        
        
        
        
        


        

