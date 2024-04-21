# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 21:34:24 2023

@author: USER
"""
# 自適化
import cv2
import numpy as np
img = cv2.imread('car2.jpg',0) # 二值化必須為灰階，否則無法轉
img = cv2.resize(img, (200,200))
_,res =cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# img2 = cv2.adaptiveThreshold(圖片, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 大小(通常為奇數)(用來平移), 常數)
# cv2.ADAPTIVE_THRESH_MEAN_C 平均
img2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 15, 3)
# cv2.ADAPTIVE_THRESH_GAUSSIAN_C el n ai6jc6
img3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 15, 3)

cv2.imshow('compare', np.concatenate((img,img2,img3), axis=1))

cv2.waitKey()
cv2.destroyAllWindows()