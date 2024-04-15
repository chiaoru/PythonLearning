# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 21:43:59 2023

@author: USER
"""

data = [80,60,70,90,49,33,89]

"""
1. 請由小至大排序 sort()
2. 請輸入數字去搜尋，並顯示有找到或沒找到
    有找到的要顯示你找了幾次，請用二分搜尋法
    
"""

data.sort()

print(data)

while True:
    
    newData = data
    
    search = int(input("請輸入欲搜尋的數字，-1離開:"))

    count = 0
    
    if search == -1:
        break
    elif search in newData:
        
        print("有", search, "這個數字!")
        
        while True:
        
            start = 0
            end = len(newData)-1 # 索引職由零開始
            
            mid = (start+end)//2
            
            google = newData[mid]
            
            if search == google:
                count += 1
                print("共搜尋", count, "次！")
                break
            
            elif search < google:
                count += 1
                newData = newData[:mid]

            else:
                count += 1
                newData = newData[mid+1:]
    
        #break
        
    else:
        print("找不到", search, "這個數字!")

    
# Binary Search 二分搜尋法