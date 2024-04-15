# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 21:46:06 2023

@author: USER
"""

"""
作業: 大樂透對獎

    1. 電腦開出 1~49 之間的 6 個號碼，不重複 --> 一維陣列
    2. 使用者可決定下 多少 注，每注由使用者輸入 1~49 的 6個號碼，不重複 -->二維陣列
    3. 兌獎顯示中了多少注(2個號碼即算中獎)


"""

# 1. 電腦開出 1~49 之間的 6 個號碼，不重複
import random

number = []

for i in range(7):
    ans =random.randint(1,49)
    
    if number.count(ans) > 0:
        ans =random.randint(1,49)
    else:
        number.append(ans)
    
number.sort()
#print(number)

# 2. 使用者可決定下 多少 注，每注由使用者輸入 1~49 的 6個號碼，不重複
times = int(input("請輸入欲下注幾次："))

userNumber = []


for a in range(1,times+1):
    timesN = []
    print("這是第 {} 注號碼，請輸入 1~49 之間的數字!" .format(a))
    
    for b in range(1,7):
        userN = int(input("請輸入您第{}注的第{}個號碼:".format(a,b)))
        
        if timesN.count(userN) > 0:
            print("這個號碼重複，請重新輸入！")
            userN = int(input("請輸入您第{}注的第{}個號碼:".format(a,b)))
            timesN.append(userN)
        
        elif userN > 49 or userN < 1:
            print("您輸入的數字不在範圍內，請輸入 1~49 之間的數字！請重新輸入：")
            userN = int(input("請輸入您第{}注的第{}個號碼:".format(a,b)))
            timesN.append(userN)
            
        else:
            timesN.append(userN)
    
    timesN.sort()
    userNumber.append(timesN)
    print()
    
for x in range(times):
    
    print("您的投注號碼如下：")    
    print("第 {} 注號碼為：" .format(x+1), userNumber[x])
    print()

# 3. 兌獎顯示中了多少注(2個號碼即算中獎)
bingoN = []

for j in range(times):
    bingo =[]
    
    for k in userNumber[j]:
        if k in number:
            bingo.append(k)
            
    bingo.sort()
    bingoN.append(bingo)
    
print("本期開獎號碼為：", number)
    
if len(bingoN) > 0:
    count = 0
    
    for i in range(times):
        print("您第 {} 對中的獎號為：" .format(i+1))
        print(bingoN[i])
        print()
        
        if len(bingoN[i]) >= 2:
            count += 1
            print("恭喜您第{}注對中2個以上(含)號碼，可以領獎！" .format(i+1))
            print()
        
        else:
            print("差一點就能領獎了，再接再厲！")
            print()
            
else:
    print("真可惜，沒有對中任何號碼，請再接再厲！")
    
print("本期共對中 {} 注！" .format(count))


            