from MongoDB import MongoDB_profile
from linebot import LineBotApi
import os
from linebot.models import *


class LineBot:
    def __init__(self, ID, event, msg) -> None:
        self.line_bot_api = LineBotApi(os.getenv("LINE_BOT_API_TOKEN"))
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
