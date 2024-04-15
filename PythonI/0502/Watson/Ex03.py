# -*- coding: utf-8 -*-
"""
Created on Tue May  2 19:31:28 2023

@author: USER
"""

class Role:
    def __init__(self,name,hp):
        self.name = name
        self.hp = hp
        
    def fight(self):
        print('角色攻擊')
        
    def display(self):
        print('姓名：',self.name)
        print('血量：',self.hp)
        
        
        
class Adviser(Role):
    
    #重新定義  (override 覆寫)
    def fight(self):
        print('軍師扇扇攻擊')
        
    def cure(self):
        print('軍師補血大作戰')
        
        
class SwordsMan(Role):
    def fight(self):
        print('使用大劍一砍')
        
        
if __name__ == '__main__':

    adviser = Adviser('孔明',200)
    swordsman = SwordsMan('關羽',500)
    
    adviser.fight()
    adviser.cure()
    adviser.display()
    
    swordsman.display()


    Role.fight(adviser)



        







        
        
        
        
        
        
        
        