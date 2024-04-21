# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 20:24:52 2023

@author: USER
"""
# 影像處理流程
#  原圖 -> 灰階 -> 轉黑白 -> 模糊處理 -> 找邊緣 -> 截下有興趣的區域 -> 侵蝕、膨脹(讓雜訊降低) -> 影像辨識處理

import cv2
import numpy as np

img = cv2.imread('car.jpg')

# 轉灰階
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 轉二值化
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# 高斯模糊
img_blur = cv2.GaussianBlur(binary, (5,5), 0)

# 印出圖片
cv2.imshow('blur', img_blur)
cv2.waitKey()
cv2.destroyAllWindows()

# 找邊緣 cv2.findContours(來源, 抓取內容, 抓取方法)
contours, hierarchy = cv2.findContours(img_blur, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 網路解釋
# https://www.cnblogs.com/wojianxin/p/12602490.html

# 抓取內容
# RETR_EXTERNAL 只偵測外層輪廓
# RETR_LIST 偵測所有的輪廓，沒有層級
# RETR_CCOMP 偵測所有的輪廓，並建立兩層級
# RETR_TREE 偵測所有的輪廓，並建立完整的層級

# 抓取方式
# CHAIN_APPROX_NONE 抓取不規則的點位，例如圓形
# CHAIN_APPROX_SIMPLE 抓取四邊矩形的位置(矩形的四點位置) -> 有固定點位的都可用，如三角形

# 找方框，找出四角位置
x, y, w, h = cv2.boundingRect(contours[0])

# 印出邊緣位置(x軸,y軸, 寬,高)
print('x=', x)
print('y=', y)
print('w=', w)
print('h=', h)

n = len(contours)

contoursImg = list()
for item in range(n):
    # 創一個跟原圖一樣大的黑底圖
    temp = np.zeros(img.shape, np.uint8)
    # 加進暫存
    contoursImg.append(temp)
    # 印出面積
    # contourArea 畫邊緣框面積
    print(cv2.contourArea(contours[item]))
    
    # 如果面積大於300
    if cv2.contourArea(contours[item]) > 300:
        # 畫出邊框
        # cv2.drawContours(要畫框的圖來源, 邊緣數據, 要畫哪一個邊框(-1為全畫),顏色,線框粗細)
        #ret = cv2.drawContours(contoursImg[item], contours, item, (0,0,255), 3)
        # 用原圖畫
        ret = cv2.drawContours(img, contours, item, (0,0,255), 3)
        # 'img'+str(item) 可能有多張
        cv2.imshow('img'+str(item),ret)

cv2.waitKey()
cv2.destroyAllWindows()