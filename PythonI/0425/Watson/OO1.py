# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Clothes(object):
    def water(self):
        print('衣服防潑水')
        
    def setColor(self,color):
        self.color = color
        
        
if __name__ == '__main__':        
    myClothes = Clothes()        
    youClothes = Clothes()
    
    print(id(myClothes))
    print(id(youClothes))
    
   
    myClothes.water()
    myClothes.setColor('紅色')
    
    youClothes.setColor('白色')
    
    
    
    print(myClothes.color)
    print(youClothes.color)
