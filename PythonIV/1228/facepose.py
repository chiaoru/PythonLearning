#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 19:46:18 2023

@author: kate
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 19:29:38 2023

@author: kate
"""

from cvzone.PoseModule import PoseDetector
import cv2

cap = cv2.VideoCapture(0)
detector = PoseDetector()

while True:
    _, img = cap.read()
    img = cv2.flip(img, 1) # 1 水平翻轉, 0 垂直翻轉 -1 水平垂直翻轉
    img= detector.findPose(img)
    cv2.imshow('img', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()