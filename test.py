from flask import Flask, request, abort

from linebot.v3 import (
    WebhookHandler
)
from linebot.v3.exceptions import (
    InvalidSignatureError
)
from linebot.v3.messaging import (
    Configuration,
    ApiClient,
    MessagingApi,
    ReplyMessageRequest,
    TextMessage,
    FlexMessage,
    FlexContainer
)
from linebot.v3.webhooks import (
    MessageEvent,
    TextMessageContent
)
import certifi
import os

# Set the environment variable to point to the cacert.pem file
os.environ['REQUESTS_CA_BUNDLE'] = '/Users/lipinze/Desktop/Coody/.venv/lib/python3.10/site-packages/certifi/cacert.pem'


app = Flask(__name__)

configuration = Configuration(access_token='T2vFpDao5Oqf5Ci9EDgvsw1GV54B6VDvJCJicMbt0NtXS0FTsj+llTDe4r9oBhGcsS1pjL/lb8Ip9I5ABnMGD5AlraJfbTXfLnaCar3haGXwsdo99qnX9NYrlv9j0t4ODX4qce1iPdLOnydXOPk7wQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('b96701b5a4af4c9de6a19cbf3f59bcd5')


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
        app.logger.info("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessageContent)
def handle_message(event):
    bubble_string = """{
                    "type": "bubble",
                    "hero": {
                        "type": "image",
                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png",
                        "size": "full",
                        "aspectRatio": "20:13",
                        "aspectMode": "cover",
                        "action": {
                            "type": "uri",
                            "uri": "http://linecorp.com/"
                        }
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": "轉帳完成",
                                "size": "sm",
                                "color": "#666666"
                            },
                            {
                                "type": "text",
                                "text": "$100",
                                "size": "3xl",
                                "weight": "bold"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "margin": "lg",
                                "spacing": "sm",
                                "contents": [
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "轉入帳戶",
                                                "flex": 0,
                                                "size": "sm",
                                                "color": "#aaaaaa"
                                            },
                                            {
                                                "type": "text",
                                                "text": "00000000000000000",
                                                "flex": 1,
                                                "size": "sm",
                                                "align": "end",
                                                "color": "#666666",
                                                "wrap": true
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "轉出帳戶",
                                                "flex": 0,
                                                "size": "sm",
                                                "color": "#aaaaaa"
                                            },
                                            {
                                                "type": "text",
                                                "text": "主帳戶",
                                                "flex": 1,
                                                "size": "sm",
                                                "align": "end",
                                                "color": "#666666",
                                                "wrap": true
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "帳戶餘額",
                                                "flex": 0,
                                                "size": "sm",
                                                "color": "#aaaaaa"
                                            },
                                            {
                                                "type": "text",
                                                "text": "$10,000",
                                                "flex": 1,
                                                "size": "sm",
                                                "align": "end",
                                                "color": "#666666",
                                                "wrap": true
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "轉帳手續費",
                                                "flex": 0,
                                                "size": "sm",
                                                "color": "#aaaaaa"
                                            },
                                            {
                                                "type": "text",
                                                "text": "免費 (本月優惠剩28次)",
                                                "flex": 1,
                                                "size": "sm",
                                                "align": "end",
                                                "color": "#666666",
                                                "wrap": true
                                            }
                                        ]
                                    }
                                ]
                            }
                        ]
                    },
                    "footer": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "button",
                                "style": "primary",
                                "action": {
                                    "type": "clipboard",
                                    "label": "action",
                                    "clipboardText": "hello"
                                }
                            }
                        ]
                    }
                }"""
    with ApiClient(configuration) as api_client:
        line_bot_api = MessagingApi(api_client)
    message = FlexMessage(alt_text="hello", contents=FlexContainer.from_json(bubble_string))
    print(message.to_json())
    line_bot_api.reply_message(
        ReplyMessageRequest(
            reply_token=event.reply_token,
            messages=[message]
        )
    )







if __name__ == "__main__":

    app.run(port=8080,host ="0.0.0.0")
