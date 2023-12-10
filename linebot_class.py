from MongoDB import MongoDB_profile
from MongoDB import activated_DB as temp_DB
from linebot import LineBotApi
import os
from linebot.models import *

from MongoDB.students_DB import student_DB as stu_DB
from MongoDB.professors_DB import professor_DB as pro_DB
import logging as log
import dotenv
from MongoDB import activated_DB as act_DB

# Send gmail
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class LINEBOT:
    def __init__(self, id, event, msg) -> None:
        dotenv.load_dotenv()
        self.event = event
        self.id = id
        self.msg = msg
        self.line_bot_api = LineBotApi(os.getenv("LINE_BOT_API_TOKEN"))
        profile = act_DB.check_profile(id)
        self.status = profile["status"]
        self.level = profile["level"]
        self.identity = profile["identity"]

    def reply_msg(self, msg) -> None:
        self.line_bot_api.reply_message(
            self.event.reply_token, TextSendMessage(text=msg))

    def push_msg(self, msg) -> None:
        self.line_bot_api.push_message(self.id, TextSendMessage(text=msg))

    def find_stu_and_pro_DB(self, id, attributes=["stu_name", "stu_gender", "stu_id", "stu_subject", "mail", "activation_code", "status", "level", "identity"]) -> dict:
        student = stu_DB.find_student_by_userid(id, attributes)
        professor = ['none']
        if not student and professor:
            return professor
        elif student and not professor:
            return student
        else:
            log.error("find_stu_and_pro_DB error")

    def send_activation_email(slef, recipient_email, activation_code):
        # SMTP 服務器設置（以 Gmail 為例）
        smtp_server = "smtp.gmail.com"
        smtp_port = 587  # 對於 TLS
        username = "cjjs0322@gmail.com"
        password = "oiel lzxv ajpy kper"  # TODO:把東西放到.env裡面

        # 創建郵件對象
        msg = MIMEMultipart()
        msg['From'] = username
        msg['To'] = recipient_email
        msg['Subject'] = "您的啟動碼"

        # 郵件正文
        body = f"您的啟動碼是：{activation_code}"
        msg.attach(MIMEText(body, 'plain'))

        # 建立 SMTP 連接
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # 啟動 TLS 加密

        # 登入 SMTP 服務器
        try:
            server.login(username, password)
            # 發送郵件
            server.sendmail(msg['From'], msg['To'], msg.as_string())

        except smtplib.SMTPAuthenticationError:
            log.error("Error: Authentication failed")

        # 斷開連接
        server.quit()

    def update_status(self, status):
        act_DB.update_status(self.id, status)
