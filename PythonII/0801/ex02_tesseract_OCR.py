# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 19:58:16 2023

@author: USER
"""

# OCR 安裝位址
#https://digi.bib.uni-mannheim.de/tesseract/

from PIL import Image # 開啟圖片
import pytesseract

fileName = 'car2.jpg'

# r 不用理會中間的特殊符號，如 \n跳行
pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files\Tesseract-OCR\tesseract.exe"

img = Image.open(fileName)
text = pytesseract.image_to_string(img, lang='eng', config="-c tessedit_char_whitelist=0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ --psm 12")
# --psm 自動頁面分割模式 參數0-13

print(text.strip())

# 白名單
#-c tessedit_char_whitelist=0123456789 


