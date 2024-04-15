# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 21:20:11 2023

@author: USER
"""
# Flask

from flask import Flask

app = Flask(__name__) #__name__ 主程式

@app.route("/")
def index():
    return "這是首頁"

@app.route("/news")
def news():
    return "新聞"

app.run()