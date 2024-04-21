# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 18:37:10 2023

@author: USER
"""

# 高斯模糊 GaussianBlur
import cv2
import numpy as np

img = cv2.imread('car2.jpg', cv2.IMREAD_COLOR)

# cv2.GaussianBlur(來源影像, 指定區域單位 ksize (須為大於1的奇數), 方向偏移量(預設為0))
img_blur = cv2.GaussianBlur(img, (1,1), 0)

img_blur2 = cv2.GaussianBlur(img, (3,3), 0)

cv2.imshow('compare', np.concatenate((img,img_blur,img_blur2), axis=1))

cv2.waitKey()
cv2.destroyAllWindows()