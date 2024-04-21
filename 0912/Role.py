# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 20:30:19 2023

@author: USER
"""



class Role:
    def __init__(self, name, hp, mp):
        self.__name = name
        self.__hp = hp
        self.__mp = mp
        
    def fight(self):
        pass
    
    def getName(self):
        return self.__name
    
    def getHP(self):
        return self.__hp
    
    def getMP(self):
        return self.__mp
    
    def changeHP(self, hp): # 因為私有化，所以要另外指定
        self.__hp -= hp
        
    def changeMP(self, mp):
        self.__mp -= mp