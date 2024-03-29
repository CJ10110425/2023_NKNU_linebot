from MongoDB import MongoDB_profile
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
import os
import init
from Pro_function import pro_functions
import linebot_class

class LineBotApp:
    def __init__(self):
        self.app = Flask(__name__)
        self.handler = WebhookHandler(os.getenv("CHANNEL_SECRET"))
        self.line_bot_api = LineBotApi(os.getenv("LINE_BOT_API_TOKEN"))
        self.setup_routes()

    def setup_routes(self):
        @self.app.route("/callback", methods=['POST'])
        def callback():
            signature = request.headers['X-Line-Signature']
            body = request.get_data(as_text=True)
            self.app.logger.info("Request body: " + body)
            try:
                self.handler.handle(body, signature)
            except InvalidSignatureError:
                abort(400)
            return 'OK'

        @self.handler.add(MessageEvent, message=TextMessage)
        def handle_message(event):
            linebot = linebot_class.LINEBOT(
                event.source.user_id, event, event.message.text)
            print(linebot.identity) #TODO:delete
            match linebot.identity:
                case "visitor":
                    init.visitor(linebot)
                case "professor":
                    pro_functions.professor(linebot)
                case "student":
                    # go to Student Doc
                    pass

    def run(self, host='0.0.0.0', port=80):
        self.app.run(host, port)


def main():
    app = LineBotApp()
    port = int(os.environ.get('PORT'))
    app.run(port=port)


if __name__ == "__main__":
    main()
