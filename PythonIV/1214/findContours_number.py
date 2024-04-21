# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 19:19:19 2023

@author: USER
"""

import cv2

import numpy as np

img = cv2.imread('number.png')
#    img = cv2.imread('money.jpg')

# 轉灰階
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 高斯模糊
blur = cv2.GaussianBlur(gray, (5,5), 1)

# 二值化
thresh = cv2.adaptiveThreshold(blur, 255, 1, 1, 11, 2)

# 找邊緣
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
#contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for c in contours:
    print(cv2.contourArea(c))
    # 如果邊框面積大於50
    if cv2.contourArea(c) > 50:
        # 找四邊
        [x,y,w,h] = cv2.boundingRect(c)
        # 如果高大於28時 (從小畫家量)
        if h > 28:
            # 畫方框
            #cv2.rectangle(img, rec, color)
            # cv2.rectangle(img, 起始點, 終止點, 顏色, 粗細)
            cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,255), 2)
            cv2.imshow('img', img)
            cv2.waitKey()
            
cv2.waitKey()
cv2.destroyAllWindows()
            
