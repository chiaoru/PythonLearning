# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 18:51:53 2023

@author: USER
"""

import cv2

# 圖片讀取
img = cv2.imread('car.jpg')
# 轉灰階
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 做高斯模糊
blur = cv2.GaussianBlur(gray, (5,5), 1)
# 二值化
#cv2.adaptiveThreshold(src, maxValue, adaptiveMethod, thresholdType, blockSize, C)
# adaptiveMethod -> 平均 0 高斯 1
# thresholdType -> BRI 0 INV 1 
thresh = cv2.adaptiveThreshold(blur, 255, 1, 1, 11, 3)

# 找邊緣
#偵測所有的輪廓，沒有層級
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
# 只偵測外層輪廓
#contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#偵測所有的輪廓，並建立兩層級
#contours, hierarchy = cv2.findContours(thresh, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
#偵測所有的輪廓，並建立完整的層級
#contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# 畫邊緣
cv2.drawContours(img, contours, -1, (0,0,255), 3)
# 呈現圖片
cv2.imshow('img', img)

cv2.waitKey()
cv2.destroyAllWindows()



