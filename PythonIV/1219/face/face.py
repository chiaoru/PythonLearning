# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 20:07:30 2023

@author: USER
"""

import cv2

# 臉部分類器
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread('img/006.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.05, 3, maxSize=(250,250)) # 比例 1.01 偵測3次 才確定是人臉

for (x,y,w,h) in faces:
    im = cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,255), 3)
    
cv2.imshow('img',im)
cv2.waitKey()
cv2.destroyAllWindows()
