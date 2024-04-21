#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 19:56:29 2023

@author: kate
"""

# https://steam.oxxostudio.tw/category/python/ai/ai-mediapipe-pose.html

import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)
mp_drawing = mp.solutions.drawing_untils
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)

while cap.isOpened():
    _, img = cap.read()
    img =cv2.cvtColor(cv2.flip(img,1),cv2.COLOR_BGR2RGB)
    result = pose.process(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    
    if result.pose_landmarks:
        mp_drawing.draw_landmarks(img, result.pose_landmarks, mp_pose.POSE_CONNECTIONS)
    
    cv2.imshow('img', img)
    cv2.waitKey()
    cv2.destroyAllWindows()