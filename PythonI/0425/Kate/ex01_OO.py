# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 18:44:58 2023

@author: USER
"""

# class 物件

class Clothes(object): # object 可省略不寫
    
    def water(self): # 物件中第一字一定為 self
        print('衣服防潑水')
        
    def setColor(self, color):
        self.color = color
        
if __name__ == '__main__':
    myClothes = Clothes()
    yourClothes = Clothes()
    
    print(id(myClothes))
    print(id(yourClothes))

    myClothes.water()
    myClothes.setColor('紅色')

    yourClothes.setColor('白色')

    print(myClothes.color) 
    print(yourClothes.color)       
    