# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 21:35:55 2023

@author: USER
"""

import cv2

img = cv2.imread('lena.jpg')

b = img[:,:,0] # 冒號為全抓

g = img[:,:,1]

r = img[:,:,2]

cv2.imshow('b', b)
cv2.imshow('g', g)
cv2.imshow('r', r)

# 將g與b 轉成0 => 變成紅色
img[:,:,0]=0
img[:,:,1]=0
cv2.imshow('lena',img)

cv2.waitKey()
cv2.destroyAllWindows()