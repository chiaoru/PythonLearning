# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 18:28:37 2023

@author: USER
"""

from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageSendMessage
)

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('Bcg4ZFQ/I3CwbyK3HF/uE/XuUhrnSo0Klf9KjntYBJ0aU4wWfZ7fGYsibiN4JrVg8BV0VWiP6hugWlHCj9wFFvP5xWrg4SXOgBihop6sIfplUEYGAExiEDy4B70al/iiEzMAiMAVaSy2I0YSeTSM8AdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('76969b4724d5c368ec7f3b7d7cdddeb7')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

def getInfo(word):
    content = {'蘋果':'醫生遠離我!','皮衣':'有名的黃先生','聯成':'電腦補習班'}
    return content.get(word,'無法理解')


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    
    linemsg = event.message.text # 接收到line傳來的訊息
    msgtype = 1
    
    if "chatGPT" in linemsg:
        response = getGPT()
        
    elif "圖片" in linemsg:
        
        msgtype = 2 
        
    else:
        response = getInfo(linemsg)
    
    if msgtype == 1:
        message = TextSendMessage(text=response)
        
    elif msgtype == 2:
        message = ImageSendMessage(original_content_url='https://i.discogs.com/YCopd9B5j4KEu0_mA-L8GirzXpRoHKAFJjDEkntsRTM/rs:fit/g:sm/q:90/h:600/w:600/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9BLTIyMjYz/MDYtMTU5NzMzMjM5/Mi03MzMwLmpwZWc.jpeg', preview_image_url='https://i.discogs.com/YCopd9B5j4KEu0_mA-L8GirzXpRoHKAFJjDEkntsRTM/rs:fit/g:sm/q:90/h:600/w:600/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9BLTIyMjYz/MDYtMTU5NzMzMjM5/Mi03MzMwLmpwZWc.jpeg')
        
    line_bot_api.reply_message(
        event.reply_token,
        message)

import os

from chatGPT  import getGPT


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
