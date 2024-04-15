# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 21:20:11 2023

@author: USER
"""
# Flask

from flask import Flask, render_template
from ctsNews import getNews

app = Flask(__name__) #__name__ 主程式

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/news")
def news():
    
    allnews = getNews()
    return render_template("news.html", **locals())

app.run()