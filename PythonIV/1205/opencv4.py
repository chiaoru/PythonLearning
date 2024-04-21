# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 20:05:00 2023

@author: USER
"""

import cv2

img = cv2.imread('lena.jpg')
for i in range(100,200):
    for x in range(100,200):
        img[i,x] = 0
        # img[i,x] x # 打碼
        
cv2.imshow('lena', img)
cv2.waitKey()
cv2.destroyAllWindows()