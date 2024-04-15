# -*- coding: utf-8 -*-
"""
Created on Thu May 11 20:51:34 2023

@author: USER
"""

import openpyxl

wb = openpyxl.Workbook()

ws = wb.active

ws.title = 'member'

wb.save('lcc.xlsx')