# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 19:14:17 2023

@author: USER
"""
# 高斯模糊
import cv2
import numpy as np
img = cv2.imread('car2.jpg',0) 
img = cv2.resize(img, (400,400))
_,res =cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

img_blur = cv2.GaussianBlur(res, (1,1), 0)

img_blur2 = cv2.GaussianBlur(res, (3,3), 0)

cv2.imshow('compare', np.concatenate((img,img_blur,img_blur2), axis=1))

cv2.waitKey()
cv2.destroyAllWindows()