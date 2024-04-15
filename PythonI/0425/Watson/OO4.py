# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 21:20:28 2023

@author: USER
"""

import math

class Circle():
    def __init__(self,radius = 6):
        self.radius = radius
        
    def roundArea(self):
        return self.radius * self.radius * math.pi
    
    def calcPerimeter(self):
        return 2 * self.radius * math.pi
    
    
    
if __name__ == '__main__':
    cir = Circle(12)    
    print('半徑：',cir.radius)
    print('圓周長{:.2f}'.format(cir.calcPerimeter()))
    print('圓面積{:.2f}'.format(cir.roundArea()))
    
    
    cir2 = Circle()    
    print('半徑：',cir2.radius)
    print('圓周長{:.2f}'.format(cir2.calcPerimeter()))
    print('圓面積{:.2f}'.format(cir2.roundArea()))    
    
    
    
    