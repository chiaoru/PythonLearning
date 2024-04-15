# -*- coding: utf-8 -*-
"""
Created on Tue May  2 19:19:43 2023

@author: USER
"""

class Role:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        
    def fight(self):
        print('角色攻擊')
        
    def display(self):
        print('姓名:', self.name)
        print('血量:', self.hp)
        
# 可將重複的程式 提昇 給予父類別，可以簡化程式碼
class Adviser(Role): 
    # 重新定義 (override 覆寫)
    def fight(self):
        print('軍師扇扇攻擊')
        
    def cure(self):
        print('軍師補血大作戰')
        
class SwordsMan(Role):
    def fight(self):
        print('用大劍一砍')
        
if __name__ == '__main__':
    
    adviser = Adviser('孔明', 100)
    swordsman = SwordsMan('關羽', 500)
    
    adviser.fight() # 當自己有的時候，先用自己的
    adviser.cure()
    adviser.display()
    
    swordsman.display()
    
    Role.fight(adviser) # 因為adviser是物件，所以可以放進self的位置去跑，但結果只是Role中的fight