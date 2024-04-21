# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 19:29:27 2023

@author: USER
"""

# 侵蝕與膨脹
import cv2
import numpy as np

img = cv2.imread('car.jpg')
gray =cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#_,res =cv2.threshold(gray, 127, 250, cv2.THRESH_BINARY)
# 用cv2.THRESH_BINARY_INV 在此圖中更明顯
_,res =cv2.threshold(gray, 127, 250, cv2.THRESH_BINARY_INV)

kernel = np.ones((5,5), np.uint8)

# 消除雜點，更易於辨識
# 侵蝕：會先將白色的移除(黑色變多) => 會有小白點不見 (字變瘦)
img2 = cv2.erode(res, kernel)
# (接續侵蝕做)膨脹：可以再讓小白點消失 (字還原大小)
img3 = cv2.dilate(img2, kernel)

cv2.imshow('res', res)
cv2.imshow('erode', img2)
cv2.imshow('dilate', img3)

cv2.waitKey()
cv2.destroyAllWindows()

