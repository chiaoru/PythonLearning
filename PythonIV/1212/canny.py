# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 20:02:36 2023

@author: USER
"""

import cv2
import numpy as np
img = cv2.imread('car2.jpg')
img = cv2.resize(img, (300,300))
#轉灰階
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 高斯模糊
img_blur = cv2.GaussianBlur(gray, (15,15), 0)
# 找邊緣 cv2.Canny(img_blur, 二值化邊緣起始值, 二值化邊緣終止值)
# 官方建議最佳為1:2或1:3
img_canny = cv2.Canny(img_blur, 30, 60)

img_canny2 = cv2.Canny(img_blur, 30, 90)
# 以車牌來說，1:5拉大會比較ok(完整性邊緣為主)
img_canny3 = cv2.Canny(img_blur, 30, 150)

cv2.imshow('comapre', np.concatenate((gray,img_blur,img_canny,img_canny2,img_canny3), axis=1))

cv2.waitKey()
cv2.destroyAllWindows()