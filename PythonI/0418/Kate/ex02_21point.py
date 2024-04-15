# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 19:36:13 2023

@author: USER
"""

# 範例 二十一點

import random

cards = list()

for i in range(1,14): # 從一點到十三點
    for y in range(1,5): # 一個點數有四張
        cards.append(i) # 共52張牌
        
def giveCards():
    point = cards.pop(0) # 抓第一個, 因為pop會抓出不放回
    if point >= 10:
        point = 10
    return point
        
def washCard(cards):
    for i in range(200):
        first = random.randint(0,len(cards)-1) # 因為從0開始所以要-1
        end = random.randint(0,len(cards)-1) 
        cards[first], cards[end] = cards[end], cards[first]


#print(cards) #洗牌前
washCard(cards) # 洗牌後
#print(cards) 


print("Welcome to 21!")
print('-'*30)

myMoney = 100

while myMoney > 0:
    
    gamePoint = myMoney    
    
    while True:
        gamePoint = int(input('請輸入欲下注的代幣數:'))
        if gamePoint > myMoney:
            print("代幣不足，目前代幣為:", myMoney)
        else:
            break
    
    print()
    print()
    print("您的下注金額為:", gamePoint)
    
    NPC = list()
    player = list()
    
    NPC.append(giveCards())
    print("莊家 ? 點") #莊家第一張蓋牌
    
    player.append(giveCards())
    print("玩家", player[0], "點")
    
    print('-'*30)
    
    NPC.append(giveCards())
    print("莊家:", NPC[1], "點")
    
    player.append(giveCards())
    print("玩家", player[1], "點")
    
    print('目前玩家總點數:', sum(player))
    print('-'*30)
    
    q = 'y' # 預設要補牌
    i = 2 # 前面已發過兩張牌
    
    while q == 'y': # 預設要補牌
        q = input("請問玩家要加牌嗎(y/n):")
        if q != 'y':
            break
        player.append(giveCards())
        print("玩家:", player[i], "點")
        print("玩家總點數:", sum(player))
        i += 1 # 補玩牌
        
        if sum(player) > 21:
            print("玩家爆了!")
            break
        elif sum(player) == 21:
            break
    
    print("莊家總點數:", sum(NPC))
    
    # 莊家補牌
    if sum(player) < 21: 
        
        i = 2
        while sum(NPC) <= sum(player): # 當NPC加總小於玩家要補牌
            NPC.append(giveCards())
            print("莊家點數為:", NPC[i], "點")
            print("莊家總點數為:", sum(NPC))
            i += 1
            
    # 判斷誰獲勝
    if sum(player) < 21:
        if sum(NPC) > 21 or sum(NPC) < sum(player):
            myMoney += gamePoint
            print("莊家輸了!")
            
        elif sum(NPC) == 21 or sum(NPC) > sum(player):
            myMoney -= gamePoint
            print("莊家贏了!")
            
        # 玩家過五關
        elif len(player) == 5 and sum(player) <= 21:
            myMoney += gamePoint*3
            
    elif sum(player) >21:
        myMoney -= gamePoint
        print("玩家爆了!")
        
    # 玩家莊家都是21點時，莊家贏
    elif sum(player) == sum(NPC):
        myMoney -= gamePoint
        print("莊家贏了!")
    
    #莊家過五關
    elif len(NPC) == 5 and sum(NPC) <= 21:
        myMoney -= gamePoint*2
        

    
    print()
    print('-'*30)
    
    print("目前剩餘:", myMoney, "元")
    q = input("繼續請按 y:")
    if q != 'y':
        break
    
    # 如果沒牌要重新拿牌蹦並洗牌
    
# 相同概念也可做十點半
    
    
        
            
        
            
        
            
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

