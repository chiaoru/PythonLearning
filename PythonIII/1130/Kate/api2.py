# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 21:22:48 2023

@author: USER
"""
from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)
allgoods = [
    {'id':10, 'name':'海底撈', 'price':999},
    {'id':99, 'name':'鼎王', 'price':99},
    ]

class Product(Resource):
    def get(self):
        return {'goods':{'status':'success','product':allgoods}},200

    def post(self):
        return "post"

api.add_resource(Product, '/goods')

if __name__ == '__main__':
    app.run(port=5566, debug=True)


