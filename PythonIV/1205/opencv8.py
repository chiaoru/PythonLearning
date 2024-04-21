# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 21:21:56 2023

@author: USER
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 20:58:03 2023

@author: USER
"""

import cv2
import numpy as np

img = cv2.imread('lena.jpg')

#轉換顏色
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 同時show出圖片
cv2.imshow('img', np.concatenate((img, rgb), axis=1)) # axis=1 水平排列 0 垂直排列
# 因為灰階只有兩個通道(2維)，所以無法對應三通道(3維)陣列

cv2.waitKey()
cv2.destroyAllWindows()