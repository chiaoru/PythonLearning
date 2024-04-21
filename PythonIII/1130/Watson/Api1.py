# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 21:03:53 2023

@author: USER
"""

from flask import Flask

app = Flask(__name__)

allgoods = [
    {"id":50,"name":"海底撈","price":999},
    {"id":100,"name":"鼎王","price":99}
    ]


@app.route("/getGoods")
def goods():
    return {"goods":{"status":"success","product":allgoods}},200

if __name__ == '__main__':
    app.run(port=5566,debug=True)