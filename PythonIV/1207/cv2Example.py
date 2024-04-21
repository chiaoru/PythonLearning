# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 18:45:01 2023

@author: USER
"""

import cv2
import numpy as np

# 裁切

def crop_img(img):
    print('圖片', img.shape)
    cv2.imshow('img', img)
    # 裁切一半
    half = int(img.shape[1]/2)
    crop = img[:,half:half+100,:]
    cv2.imshow('cropimg',crop)
    
    cv2.waitKey()
    cv2.destroyAllWindows()
    
# 等比例縮放圖
def resize_img(img):
    print('原圖：',img.shape)
    # cv2.resize(原圖位置, (寬,高))
    imgresize = cv2.resize(img, (200,200))
    cv2.imshow('resize', imgresize)
    print('縮放圖後：', imgresize.shape)
    cv2.waitKey()
    cv2.destroyAllWindows()
    
# 調明暗
def change_bright(img, bright):
    rows, cols, channels = img.shape # 確保為彩色圖
    # 目的地
    dst = img.copy()
    for i in range(rows):
        for x in range(cols):
            for c in range(channels):
                color = img[i,x][c]+bright
                # 亮度在0~255 之間
                # 不做判斷時，圖很怪
                if color > 255:
                    dst[i,x][c] = 255
                elif color < 0:
                    dst[i,x][c] = 0
                else:
                    dst[i,x] = color
    return dst
    
# 調對比
def change_contrast(img, contrast):
    rows, cols, channels = img.shape # 確保為彩色圖
    # 目的地
    dst = img.copy()
    for i in range(rows):
        for x in range(cols):
            for c in range(channels):
                color = img[i,x][c]*contrast
                # 亮度在0~255 之間
                # 不做判斷時，圖很怪
                if color > 255:
                    dst[i,x][c] = 255
                elif color < 0:
                    dst[i,x][c] = 0
                else:
                    dst[i,x] = color
    return dst
    

if __name__ == '__main__':
    img = cv2.imread('lena.jpg')
    img2 = cv2.imread('photo.jpg')
    img3 = cv2.imread('poniu.jpg')
    #crop_img(img)
    #crop_img(img2)
    
    #resize_img(img)
    #resize_img(img2)
    
    resize = cv2.resize(img, (200,200))
    up = change_bright(resize, 100)
    down = change_bright(resize, -100)
    cv2.imshow('bright', np.concatenate((up,resize,down), axis=1))
    
    resize2 = cv2.resize(img3, (250,150))
    up2 = change_contrast(resize2, 1.5)
    down2 = change_contrast(resize2, 0.5)
    cv2.imshow('contrast', np.concatenate((up2,resize2,down2), axis=1))
    cv2.waitKey()
    cv2.destroyAllWindows()
    
    
    