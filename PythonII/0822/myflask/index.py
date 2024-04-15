# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 21:20:11 2023

@author: USER
"""
# Flask

from flask import Flask, render_template
from ctsNews import getNews
import db

app = Flask(__name__) #__name__ 主程式

@app.route("/")
def index():
    allnews = getNews()[:5]
    
    sql = "select * from product order by id desc limit 4"
    db.cursor.execute(sql)
    allGoods = db.cursor.fetchall()
    
    sql = "select create_date, name, photo_url, link from food order by create_date limit 5"
    db.cursor.execute(sql)
    db.connect.commit()
    food = db.cursor.fetchall()
    
    return render_template("index.html", **locals())

@app.route("/news")
def news():
    
    allnews = getNews()
    return render_template("news.html", **locals())

@app.route("/product")
def PChome():
    
    sql = "select * from product order by id desc"
    db.cursor.execute(sql)
    allGoods = db.cursor.fetchall()
    
    return render_template("product.html", **locals())


@app.route("/food")
def food():
    sql = "select create_date,name,photo_url,link from food order by create_date"
    db.cursor.execute(sql)
    db.connect.commit()
    food = db.cursor.fetchall()
    return render_template("food.html", **locals())

"""
@app.route("/rate")
def rate():
    return render_template("rate.html", **locals())



@app.route("/contact")
def contact():
    return render_template("contact.html", **locals())
"""
app.run()