# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 19:19:19 2023

@author: USER
"""

import cv2

img = cv2.imread('lena.jpg') # 讀檔

cv2.imshow('img', img) # 秀在螢幕上
cv2.waitKey() # 等待任意鍵，按一鍵即關閉
cv2.destroyAllWindows() # 必須做，否則Spyder當掉