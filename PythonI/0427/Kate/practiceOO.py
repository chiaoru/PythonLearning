# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 21:29:35 2023

@author: USER
"""
#  第一種角色: 劍士
class SwordsMan: 
    def __init__(self, name, hp, level):
        self.__name = name
        self.__hp = hp
        self.__level = level
        
    def fight(self):
        print(self.__name, '使用三刀流')
        
    def skill(self):
        print(self.__name, '使出星爆大亂砍')
        
    def changeHP(self, hp):
        self.__hp -= hp
        return self.__hp
    
    def getHP(self):
        return self.__hp
    
    def getName(self):
        return self.__name

# 第二種角色: 舞者
class Dancer:
    def __init__(self, name, hp, level):
        self.__name = name
        self.__hp = hp
        self.__level = level
        
    def fight(self):
        print(self.__name, '使用圓舞')
        
    def skill(self):
        print(self.__name, '使出戰舞')
            
    def cure(self):
        print(self.__name, '使出補血')
        
    def changeHP(self, hp):
        self.__hp -= hp
        return self.__hp
    
    def getHP(self):
        return self.__hp
    
    def getName(self):
        return self.__name
    
# 第三種角色: 軍師
class Adviser:
    def __init__(self, name, hp, level):
        self.__name = name
        self.__hp = hp
        self.__level = level
        
    def fight(self):
        print(self.__name, '使出扇子攻擊')
    
    def skill(self):
        print(self.__name, '火龍計')
        
    def cure(self):
        print(self.__name, '使出補血')
        
    def trick(self):
        print(self.__name, '水淹七軍')
    
    def changeHP(self, hp):
        self.__hp = hp
        return self.__hp
    
    def getHP(self):
        return self.__hp
    
    def getName(self):
        return self.__name
    
    
    
    
    
    
    
    
    
    
        