import MongoDB_profile
# 載入LineBot所需要的套件
import os
import Init
import Pro_functions
import re
from flask import Flask, request, abort, render_template
from flask import redirect
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
app = Flask(__name__)
handler = WebhookHandler('551d866b1602853292a0c02b7ef8055c')
# 監聽所有來自 /callback 的 Post Request


@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


class LineBot:
    def __init__(self, ID, event, msg) -> None:
        self.line_bot_api = LineBotApi(
            'Orj4xNTzu4lZEwnUuf5B1Sdez01KSPtyBo1UC1ZnpPS93AMguOYc4XkQuw1BqIIDdmgITw4guIGtkJJ98w/y3sUM3MqXFQoaXtpw4bzWVuB0fxdCa3a2sGzRVS2W+HqOJOHV8BIGzl3QQe3ygcw4hAdB04t89/1O/w1cDnyilFU=')
        Profile = self.check_initial(ID)
        self.event = event
        self.ID = ID
        self.msg = msg
        self.Status = Profile["Status"]
        self.Level = Profile["Level"]
        self.Identity = Profile["Identity"]
        self.Register = Profile["Register"]

    def reply_msg(self, msg) -> None:
        self.line_bot_api.reply_message(
            self.event.reply_token, TextSendMessage(msg))

    def push_msg(self, msg) -> None:
        self.line_bot_api.reply_message(
            self.event.reply_token, TextSendMessage(msg))

    def check_initial(self, ID) -> dict:
        if MongoDB_profile.check_profil_exist(ID):  # 確認是否有使用者資料
            return MongoDB_profile.find_profile(ID)
        else:
            Profile = {"User_Id": ID, "Status": "Standard",
                       "Level": 0, "Identity": "None", "Register": "None"}
            MongoDB_profile.store_profile(Profile)
            return Profile

    def Change_Status(self, Status):
        self.Status = Status
        MongoDB_profile.update_Status(self.ID, Status)

    def Change_Level(self, Level):
        self.Level = Level
        MongoDB_profile.update_Level(self.ID, Level)

    def Change_Register(self, Register):
        self.Register = Register
        MongoDB_profile.update_Register(self.ID, Register)

    def Change_Identity(self, Identity):
        self.Identity = Identity
        MongoDB_profile.update_Identity(self.ID, Identity)


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    Linebot = LineBot(event.source.user_id, event, event.message.text)
    match Linebot.Identity:
        case "None":
            '''go to Initialization .py'''
            Linebot_init = Init._None(Linebot)
            Linebot_init.Init()
        case "Professor":
            Linebot_Professor = Pro_functions.professor(Linebot)
            Linebot_Professor.professor_function()
        case "Student":
            '''go to Student Doc'''
            
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 80))
    app.run(host='0.0.0.0', port=port)
