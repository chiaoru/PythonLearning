# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 20:48:58 2023

@author: USER
"""

import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

img = cv2.imread('img/001.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 3, minSize=(36,36))
for (x,y,w,h) in faces:
    im = cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,255), 2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_img = img[y:y+h, x:x+w]
    
    eyes = eye_cascade.detectMultiScale(roi_gray, 1.15, 3, minSize=(10,10))
    for (eye_x,eye_y,eye_w,eye_h) in eyes:
        cv2.rectangle(roi_img, (eye_x, eye_y), (eye_x+eye_w, eye_y+eye_h), (0,255,255), 3)
        
cv2.imshow('img',im)
cv2.waitKey()
cv2.destroyAllWindows()

        