# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 19:19:03 2023

@author: USER
"""

# 影像處理流程
#  原圖 -> 灰階 -> 轉黑白 -> 模糊處理 -> 找邊緣 -> 截下有興趣的區域 -> 侵蝕、膨脹(讓雜訊降低) -> 影像辨識處理

#網路解釋
# https://steam.oxxostudio.tw/category/python/ai/opencv-blur.html#a2

# 模糊
import cv2
import numpy as np
img = cv2.imread('car2.jpg',0) 
img = cv2.resize(img, (300,300))
_,res =cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# 平均模糊
blur = cv2.blur(res, (1,1))

blur2 = cv2.blur(res, (3,3))

# 中值模糊 
medianBlur = cv2.medianBlur(res, 3)

medianBlur2 = cv2.medianBlur(res, 7)

# 高斯模糊
gaussianBlur = cv2.GaussianBlur(res, (1,1), 0)

gaussianBlur2 = cv2.GaussianBlur(res, (3,3), 0)

cv2.imshow('blur', np.concatenate((img,blur,blur2), axis=1))
cv2.imshow('medianBlur', np.concatenate((img,medianBlur,medianBlur2), axis=1))
cv2.imshow('GaussianBlur', np.concatenate((img,gaussianBlur,gaussianBlur2), axis=1))

cv2.waitKey()
cv2.destroyAllWindows()