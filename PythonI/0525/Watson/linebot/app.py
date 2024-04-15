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
line_bot_api = LineBotApi('SkIdKBEVhem8bx49ufoH57KR4Kbb0St4d1CdzwzY6DyHP0xFJuFaRJTFFVNlQgtllbFisXOHGtuf/fyitIyAEimNLv50vV8hw5bYOz7uzHerXSMl1KzRtdt66RICRR41qoDUx1lcf9fql+/Y4wkAUAdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('f066952eb6651eb6494969c42b0c6938')

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
    
    linemsg = event.message.text   #接收到line傳的訊息
    content = {'聯成':'成人電腦補習班','天氣':'去中央氣象局查詢','一中街':'很多好吃的東西'}
    response = content.get(linemsg,'找不到')
    
    message = TextSendMessage(text=reaponse)
    line_bot_api.reply_message(
        event.reply_token,
        message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
