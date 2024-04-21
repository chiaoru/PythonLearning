# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 21:35:35 2023

@author: USER
"""
#做認證
from flask import Flask, jsonify, request
from flask.views import MethodView
from authlib.jose import jwt

app = Flask(__name__)
app.config['SECRET_KEY']='thisissecretkeycanselftext'

class AuthorToken(MethodView):
    def post(self):
        grant_type = request.form.get('grant_type')
        username = request.form.get('username')
        password = request.form.get('password')
        
        if grant_type is None or grant_type != 'password':
            response = jsonify(message='wrong type')
            response.status_code=400
            return response
        
        if username != 'john' or password != '123':
            response = jsonify(message='wrong username or password')
            response.status_code=400
            return response
        
        data = {}
        data['token'] = app.config['SECRET_KEY']
        return data
    
app.add_url_rule('/author_token', view_func=AuthorToken.as_view('author_token'))
        
if __name__ == '__main__':
    app.run(port=5566, debug=True)