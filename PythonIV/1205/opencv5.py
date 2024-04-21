# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 20:16:46 2023

@author: USER
"""

import cv2

img = cv2.imread('lena.jpg')

# 抓臉
face = img[220:400, 250:350]
# img[y:y+h, x:x+w] 
# 可換臉，但差異值要一樣

cv2.imshow('Face', face)
cv2.waitKey()
cv2.destroyAllWindows()