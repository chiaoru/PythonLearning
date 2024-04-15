# -*- coding: utf-8 -*-
"""
Created on Thu May 25 21:13:59 2023

@author: USER
"""
#輕量級網頁框架

from flask import Flask

app = Flask(__name__)

@app.route("/")

def index():
    return"聯成電腦"
    
@app.route("/news")

def good():
    return"這是新聞頁"  
    
@app.route("/callback/<message>")#會回傳輸入訊息

def show(message):
    return message    
    
    
app.run()




