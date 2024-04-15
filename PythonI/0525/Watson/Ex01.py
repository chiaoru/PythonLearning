# -*- coding: utf-8 -*-
"""
Created on Thu May 25 21:13:51 2023

@author: USER
"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "聯成電腦"


@app.route("/news")
def good():
    return "這個是新聞頁"

@app.route("/callback/<message>")
def show(message):
    return message



app.run()