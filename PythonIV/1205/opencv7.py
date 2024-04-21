# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 20:58:03 2023

@author: USER
"""

import cv2

img = cv2.imread('lena.jpg')

#轉換顏色
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('img', img)
key = cv2.waitKey()
if key == ord('A'):
    cv2.imshow('img', rgb)
elif key == ord('B'):
    cv2.imshow('img', gray)

cv2.waitKey()
cv2.destroyAllWindows()