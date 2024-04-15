# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 19:11:07 2023

@author: USER
"""

from oo5 import Adviser,Dancer,SwordsMan

import random

import time

if __name__ == '__main__':
    print('歡迎來到onLine 三國')
    
    player = list()
    com= list()
    
    #玩家的角色
    while len(player) < 2:
        num = int(input('1 劍士 2 舞者  3 軍師:'))
        if 0 < num < 4:
            name = input('輸入角色姓名：')
            if num == 1:
                player.append(SwordsMan(name,100,1))
            elif num == 2:
                player.append(Dancer(name,100,1))
            else:
                player.append(Adviser(name,100,1))
                
                
    #電腦的            
    role = ['張飛','關羽','陳聰明','陳美麗','西施','東施']            
    while len(com) < 2:
        num = random.randint(1,3)

        name = random.choice(role)
        if num == 1:
            com.append(SwordsMan(name,100,1))
        elif num == 2:
            com.append(Dancer(name,100,1))
        else:
            com.append(Adviser(name,100,1))                
             
    while len(player) > 0 and len(com) > 0:
        
        number = random.randint(1,100)
        if number % 2 == 0:
            p = player[random.randint(0, len(player)-1)]
            c = com[random.randint(0, len(com)-1)]
            
            if isinstance(p,Adviser):
                p.trick()
            else:
                p.fight()
            
            
            print('打向',c.getName())
            blood = c.changeHp(random.randint(1,10))
            print('剩餘血量：',blood)
            if blood <= 0:
                com.remove(c)
        else:
            p = player[random.randint(0, len(player)-1)]
            c = com[random.randint(0, len(com)-1)]
            
            c.fight()
            print('打向',p.getName())
            blood = p.changeHp(random.randint(1,10))
            print('剩餘血量：',blood)
            if blood <= 0:
                player.remove(p) 
        
        time.sleep(0.2)
                
                
    if len(player) > 0:
        print('玩家Win')
    else:
        print('電腦Win')
                
                
            
        
            
          
                
          