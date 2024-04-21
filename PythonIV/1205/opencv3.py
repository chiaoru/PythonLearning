# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 19:51:41 2023

@author: USER
"""

import cv2
import numpy as np

# 灰階圖
img = np.zeros((200,200), dtype=np.uint8)

print(img)
print(img.shape)

# 換成白色
img[50,50] = 255
img[100,100] = 255

cv2.imshow('zeros', img)
cv2.waitKey()
cv2.destroyAllWindows()

# 彩色圖
img2 = np.zeros((200,200,3), dtype=np.uint8)

print(img2)
print(img2.shape)

img2[50,50] = 180
img2[100,100] = 90

cv2.imshow('zeros', img2)
cv2.waitKey()
cv2.destroyAllWindows()