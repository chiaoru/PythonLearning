# -*- coding: utf-8 -*-
"""
Created on Thu May 25 21:13:58 2023

@author: USER
"""

from flask import Flask

app = Flask(__name__) # 啟動主要物件

@app.route("/")
def index():
    return "聯成電腦"

@app.route("/news")
def news():
    return "這是新聞頁"

# 與line bot 概念相同，只是line bot 用post加密
@app.route("/callback/<message>") # <message> 會帶字串東西回復
def show(message):
    return message

app.run()