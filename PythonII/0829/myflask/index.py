# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 21:20:11 2023

@author: USER
"""
# Flask

from flask import Flask, render_template, request, redirect, url_for
from ctsNews import getNews
from twbankRate import getRate
import db
from datetime import datetime

app = Flask(__name__) #__name__ 主程式

@app.route("/")
def index():
    allnews = getNews()[:8]
    
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
    
    startPrice = request.args.get('startPrice')
    endPrice = request.args.get('endPrice')
    
    if startPrice == None or endPrice == None or startPrice == '' or endPrice == '':  
        sql = "select * from product order by id desc"
    else:
        if startPrice.isdigit() and endPrice.isdigit():
            sql = "select * from product where onsale >={} and onsale <={} order by onsale".format(startPrice, endPrice)
        else:
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

@app.route("/contact")
def message():
    return render_template("contact.html", **locals())

@app.route("/addContact", methods=['POST'])
def contact():
    if request.method == 'POST':
        username = request.form.get('name')
        title = request.form.get('title')
        email = request.form.get('email')
        content = request.form.get('content')
        
        modify_date = datetime.today()
        create_date = datetime.strftime(modify_date, '%Y-%m-%d')
        
        # 新增資料到資料表
        sql = "insert into contact(subject,name,email,content,create_date) values('{}','{}','{}','{}','{}')".format(title,username,email,content,create_date)
        db.cursor.execute(sql)
        db.connect.commit()
        
    return redirect(url_for('message'))

@app.route("/rate")
def rate():
    rate = getRate()
    return render_template("rate.html", **locals())


app.run()