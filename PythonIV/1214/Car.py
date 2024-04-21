# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 20:02:48 2023

@author: USER
"""

import numpy as np
import cv2

# 影像處理流程
#  原圖 -> 灰階 -> 轉黑白 -> 模糊處理 -> 找邊緣 -> 截下有興趣的區域 -> 侵蝕、膨脹(讓雜訊降低) -> 影像辨識處理


def load_digit_file(imgfile):
    img = cv2.imread(imgfile)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    kernel = np.ones((5,5), np.uint8)
    ret, threshold = cv2.threshold(gray, 127, 255, 0)
    # 侵蝕
    threshold = cv2.erode(threshold, kernel, 1)
    # 膨脹
    threshold = cv2.dilate(threshold, kernel, 1)
    # 找邊框
    contours, hierarchy = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # 找出有興趣的範圍
    for c in contours:
        # 面積與車牌差不多的才進來
        if cv2.contourArea(c) > 120000 and cv2.contourArea(c) < 130000:
            x,y,w,h = cv2.boundingRect(c)
            
            #畫邊框
            cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,255), 20)
            cv2.imshow('img', img)
            cv2.waitKey()
            
            # 裁圖
            newimg = threshold[y:y+h,x:x+w]
            cv2.imshow('new', newimg)
            # 存檔
            cv2.imwrite('newimg.jpg',newimg)
            
    cv2.destroyAllWindows()
    
load_digit_file('car4.jpg')
    