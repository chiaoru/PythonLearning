# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 20:37:46 2023

@author: USER
"""

import cv2

img = cv2.imread('lena.jpg')
img2= cv2.imread('photo.jpg')

# 換臉
img2[120:300, 340:440] = img[220:400, 250:350]

# 存檔
cv2.imwrite('new.jpg', img2)

cv2.imshow('Face', img2)
cv2.waitKey()
cv2.destroyAllWindows()

