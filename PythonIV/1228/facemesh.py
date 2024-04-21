#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 19:29:38 2023

@author: kate
"""

from cvzone.FaceMeshModule import FaceMeshDetetor
import cv2

cap = cv2.VideoCapture(0)
detector = FaceMeshDetetor(maxFaces=5)

while True:
    _, img = cap.read()
    img = cv2.flip(img, 1) # 1 水平翻轉, 0 垂直翻轉 -1 水平垂直翻轉
    img, bboxs = detector.findFaceMesh(img)
    cv2.imshow('img', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()