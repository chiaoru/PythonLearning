# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 20:47:47 2023

@author: USER
"""
# 二值化
import cv2
import numpy as np
img = cv2.imread('lena.jpg')
resize = cv2.resize(img, (200,200))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray2 = cv2.cvtColor(resize, cv2.COLOR_BGR2GRAY)

# t 可用 _ 取代，代表會回傳值，但不取用
#t, res = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
_, res = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
#cv2.threshold(gray灰階, 127最低, 255最高, cv2.THRESH_BINARY) 比127大設為255，比127小設為0

# 以127為閾值
# cv2.THRESH_BINARY 比127大設為255，比127小設為0
_, res0 = cv2.threshold(gray2, 127, 255, cv2.THRESH_BINARY)
# cv2.THRESH_BINARY_INV 比127大設為0，比127小設為255
_, res1 = cv2.threshold(gray2, 127, 255, cv2.THRESH_BINARY_INV)
# cv2.THRESH_TRUNC 比127大設為127，比127小時數值不變
_, res2 = cv2.threshold(gray2, 127, 255, cv2.THRESH_TRUNC)
# cv2.THRESH_TOZERO 比127大時數值不變，比127小設為0
_, res3 = cv2.threshold(gray2, 127, 255, cv2.THRESH_TOZERO)
# cv2.THRESH_TOZERO_INV 比127大設為0，比127小時數值不變
_, res4 = cv2.threshold(gray2, 127, 255, cv2.THRESH_TOZERO_INV)

cv2.imshow('img', res)
cv2.imshow('compare', np.concatenate((res0,res2,res3,res4), axis=1))
cv2.waitKey()
cv2.destroyAllWindows()