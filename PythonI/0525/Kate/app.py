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


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    
    linemsg = event.message.text # 接收到line傳來的訊息
    
    content = {"聯成":"成人電腦補習班", "天氣":"自己去中央氣象局查詢", "一中街":"很多好吃的東西"}
    
    response = content.get(linemsg,"我不明白你說的，找不到")
    
    message = TextSendMessage(text=response)
    line_bot_api.reply_message(
        event.reply_token,
        message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
