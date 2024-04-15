# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 21:29:35 2023

@author: USER
"""

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

# 第二種角色
class Dancer:
    def __init__(self, name, hp, level):
        self.__name = name
        self.__hp = hp
        self.__level = level
        
    def fight(self):
        print(self.__name, '使用圓舞')
        
    def skill(self):
        print(self.__name, '使出戰舞')\
            
    def cure(self):
        print("補血技能!")
        
    def changeHP(self, hp):
        self.__hp -= hp
        return self.__hp
    
    def getHP(self):
        return self.__hp
        