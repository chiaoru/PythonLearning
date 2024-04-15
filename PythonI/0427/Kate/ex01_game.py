# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 19:12:21 2023

@author: USER
"""

from practiceOO import Adviser, Dancer, SwordsMan

import random

import time

if __name__ == '__main__':
    print('歡迎來到 online三國')
    
    player = list()
    computer = list()
    
    # 自己產生角色帶進遊戲中
    while len(player) < 2:
        num = int(input('1 劍士 2 舞者 3 軍師:'))
        if 0 < num < 4:
            name = input('輸入角色姓名:')
            if num == 1:
                player.append(SwordsMan(name, 100, 1))
            elif num == 2:
                player.append(Dancer(name, 100, 1))
            else:
                player.append(Adviser(name, 100, 1))

    role = ['張飛','關羽','劉備','呂布','西施','小喬']
    while len(computer) < 2:
        num = random.randint(1,3)

        if 0 < num < 4:
            name = random.choice(role) # choice 是從串列中隨機挑選一個出來
            print(name)
            if num == 1:
                computer.append(SwordsMan(name, 100, 1))
            elif num == 2:
                computer.append(Dancer(name, 100, 1))
            else:
                computer.append(Adviser(name, 100, 1))
                
    # 對打
    while len(player) > 0 and len(computer) > 0:
        
        number = random.randint(1,100)
        if number % 2 == 0:
            p = player[random.randint(0,len(player)-1)] # 玩家自己挑出一個角色來打，len(player)-1 因為當一個角色死亡時，另一個角色可以繼續打
            c = computer[random.randint(0,len(computer)-1)] # 電腦資己挑出一個角色來打
            #p.fight()
            
            if isinstance(p, Adviser):
                p.trick()
            else:
                p.fight()
            
            print('打向', c.getName()) # 因為私有化的關係,所以使用getName 
            
            blood = c.changeHP(random.randint(1,20)) # 隨機扣除的血量
            print('剩餘血量:', blood)
            if blood <= 0:
                computer.remove(c) # 不能用 pop, 因為pop適用index來搜索
        
        else:
            p = player[random.randint(0,len(player)-1)] # 玩家自己挑出一個角色來打
            c = computer[random.randint(0,len(computer)-1)] # 電腦自己挑出一個角色來打
            c.fight()
            
            print('打向', p.getName()) # 因為私有化的關係,所以使用getName 
            
            blood = p.changeHP(random.randint(1,20)) # 隨機扣除的血量
            print('剩餘血量:', blood)
            if blood <= 0:
                player.remove(p) # 不能用 pop, 因為pop適用index來搜索
    
        time.sleep(0.2)
        
    if len(player) > 0:
        print('玩家 Win')
    else:
        print('電腦 Win')
        
        
        
        
        