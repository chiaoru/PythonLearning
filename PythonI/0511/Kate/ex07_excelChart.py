# -*- coding: utf-8 -*-
"""
Created on Thu May 11 21:24:11 2023

@author: USER
"""

import openpyxl

from openpyxl.chart import BarChart, Reference # chart 畫圖表使用 BarChart 長條圖

wb = openpyxl.Workbook()

ws = wb.active

sales = [['區域', '2021年','2022年'], ['台北', 31000, 29100], ['台中', 49980, 31000], ['高雄', 35970, 45600]]

for row in sales:
    ws.append(row)
    
chart = BarChart()

chart.title = '各區銷售額'
chart.x_axis.title = '地區' # x 軸刻度
chart.y_axis.title = '金額' # y 軸刻度

# Reference 填入圖表資料(範圍) 選取主要資料範圍
# min_col 最小欄位 max_col 最大欄位 min_row 最小行數 max_row 最大行數
data = Reference(ws, min_col=2, max_col=3, min_row=1, max_row=4) 

# 加入資料建立圖表
chart.add_data(data, titles_from_data=True)

# 設定出 x軸的標題
xtitle = Reference(ws, min_col=1, min_row=2, max_row=4)
chart.set_categories(xtitle)

ws.add_chart(chart, 'F1')

wb.save('chart.xlsx')

