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
line_bot_api = LineBotApi('')
# Channel Secret
handler = WebhookHandler('')

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
    
    content = {"蘋果":"醫生的最大敵人","皮衣":"有名的黃先生","聯成":"電腦補習班"}
    
    return content.get(word,"我無法理解你說的")








@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    
    linemsg = event.message.text
    

    if "空氣" in linemsg:
         response = getBike()   
    elif '圖片' in linemsg:
        response = "再找找"        
    else:
        response = getInfo(linemsg)        



    
    message = TextSendMessage(text=response)
    
    line_bot_api.reply_message(
        event.reply_token,
        message)

import os
from tnpbike import getBike
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
