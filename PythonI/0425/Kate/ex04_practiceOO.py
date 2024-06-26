# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 21:04:26 2023

@author: USER
"""

import math

class Circle(): # 第三種物件寫法
    def __init__(self, radius=6):
        self.radius = radius
        
    def roundArea(self):
        return self.radius*self.radius*math.pi
    
    def calcPerimeter(self):
        return 2*self.radius*math.pi


if __name__ == '__main__':
    circle = Circle(12)
    print('半徑:', circle.radius)
    print('圓周長{:.2f}'.format(circle.calcPerimeter()))
    print('圓面積{:.2f}'.format(circle.roundArea()))