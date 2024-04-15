# -*- coding: utf-8 -*-
"""
Created on Tue May  2 19:31:28 2023

@author: USER
"""

class Role:
    def __init__(self,name,hp):
        self.__name = name
        self.__hp = hp
        
    def fight(self):
        print('角色攻擊')
        
    def display(self):
        print('姓名：',self.__name)
        print('血量：',self.__hp)

    def getName(self):
        return self.__name
    
    def changeName(self,name):
        self.__name = name
        
        
class Adviser(Role):
    
    def __init__(self,name,hp,level):
        self.level = level
        #呼叫父類別的方式
        super().__init__(name,hp)
        
    
    #重新定義  (override 覆寫)
    def fight(self):
        print('軍師扇扇攻擊')
        
    def cure(self):
        print('軍師補血大作戰')
        
        
class SwordsMan(Role):
    def fight(self):
        print('使用大劍一砍')
        
        
if __name__ == '__main__':

    adviser = Adviser('孔明',300,5)
    swordsman = SwordsMan('關羽',500)
    
    adviser.fight()
    adviser.cure()
    adviser.display()
    
    swordsman.display()
    
    print(adviser.level)
    print(adviser.getName())
    adviser.changeName('司馬懿')
    print(adviser.getName())
    





        







        
        
        
        
        
        
        
        