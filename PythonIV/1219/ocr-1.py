# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 20:06:29 2023

@author: USER
"""

from PIL import Image
import pytesseract

fileName = "1387089134-2970851851.jpg"

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


img = Image.open(fileName)


text = pytesseract.image_to_string(img,lang='eng', config='-c tessedit_char_whitelist=0123456789QWERTYUIOPASDFGHJKLZXCVBNM --psm 12')

print(text.strip())





