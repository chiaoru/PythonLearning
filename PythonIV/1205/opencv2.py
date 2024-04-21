# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 19:31:11 2023

@author: USER
"""

import cv2

img = cv2.imread('lena.jpg', 0) # 讀檔，預設為IMREAD_COLOR

# cv2.IMREAD_COLOR 色彩圖片，但放棄透明度
# cv2.IMREAD_GRAYSCALE 灰階圖片
# cv2.IMREAD_UNCHANGED 色彩圖片，有透明度

# 灰階圖，二維(一通道)
cv2.imshow('img', img) # 秀在螢幕上
print(img.shape)
print(img)
cv2.waitKey() # 等待任意鍵，按一鍵即關閉
cv2.destroyAllWindows() # 必須做，否則Spyder當掉

# 彩圖，三維(三通道)
img2 = cv2.imread('photo.jpg')
cv2.imshow('image',img2)
print(img.shape)
print(img2)
cv2.waitKey()
cv2.destroyAllWindows() 