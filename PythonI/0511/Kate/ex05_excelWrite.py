# -*- coding: utf-8 -*-
"""
Created on Thu May 11 20:46:52 2023

@author: USER
"""

import openpyxl

# 建立空白迴頁簿
wb = openpyxl.Workbook()

ws = wb.active

# 將工作表名稱改成member
ws.title = 'member'

wb.save('lcc.xlsx')