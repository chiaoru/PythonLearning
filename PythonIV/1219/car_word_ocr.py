# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 20:59:08 2023

@author: USER
"""

# 把車牌內的文字拆解
import cv2
import pytesseract
import numpy as np

binary_threshold = 100

spacing = 0.95

img = cv2.imread('car2.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 二值化
_, ret = cv2.threshold(gray, binary_threshold,255, 1) # 0 白底黑字

cv2.imshow('img', ret) # 黑底白字

white = []
black = []
height = img.shape[0]
width = img.shape[1]
print(width, height)
white_max = 0
black_max = 0
count = 0

for i in range(width):
    w_count = 0
    b_count = 0
    
    for x in range(height):
        if ret[x][i] == 255:
            w_count += 1
        else:
            b_count += 1
    
    white_max = max(white_max, w_count)
    black_max = max(black_max, b_count)
    white.append(w_count)
    black.append(b_count)

print(white)    
print()
print(black)

kernel = np.ones((5,5), np.uint8)
print('w_max:', white_max)
print('b_max:', black_max)


arg = black_max > white_max # 黑底白字

def find_end(start_):
    end_ = start_+1
    for m in range(start_+1, width-1):
        if (black[m] if arg else white[m]) > (spacing*black_max if arg else spacing*white_max):
            end_ = m
            break
        
    return end_


n = 1
start = 1
end = 2
while n < width-1:
    n += 1
    if (white[n] if arg else black[n]) > ((1-spacing)*white_max if arg else (1-spacing)*black_max):
        start = n
        end = find_end(start)
        n = end
        if end - start > 12:
            i += 1
            print(start, end)
            cm = img[1:height, start-10:end+10]

            cv2.imwrite(str(i)+".jpg",cm)
            
            img = cv2.imread(str(i)+".jpg")

            gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                        
            ret,threshold = cv2.threshold(gray,127,255,0)
            
            threshold = cv2.erode(threshold,kernel,1)
            threshold = cv2.dilate(threshold,kernel,1)         
            
            cv2.imshow('frame',threshold)
            cv2.waitKey()            

            pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
            
            
            
            text = pytesseract.image_to_string(threshold,lang='eng', config='-c tessedit_char_whitelist=0123456789QWERTYUPLKJHGFDSAZXCVBNM --psm 10  ')
            
            print(text.strip())   
        
cv2.waitKey()
cv2.destroyAllWindows()



