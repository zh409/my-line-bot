from flask import Flask, request
from linebot import LineBotApi, WebhookHandler
from linebot.models import MessageEvent, TextMessage, TextSendMessage, FlexSendMessage
import os

app = Flask(__name__)

# 從環境變數讀取，部署到 Heroku 不會暴露密碼
LINE_CHANNEL_ACCESS_TOKEN = os.environ.get("LINE_CHANNEL_ACCESS_TOKEN")
LINE_CHANNEL_SECRET = os.environ.get("LINE_CHANNEL_SECRET")

line_bot_api = LineBotApi(DwYxJ9Vdir9I0r7OX98pDf10P/PaKeKz9KnhSQzzsjYzOs8D3DDAPkwYJ0RNHfK2b+QaB2MIHM/3NjLf7oxtCkOOkM/xv6Ti5YefId9Jhn4mczAMFjABHZhsZDlyIr2ojXmNAM+YmNgrFGcPRDp39AdB04t89/1O/w1cDnyilFU=)
handler = WebhookHandler(5ea74ec08962674867db6de8e2fac936)

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers.get('X-Line-Signature')
    body = request.get_data(as_text=True)

    print("====收到請求====")
    print("Body:", body)
    print("Signature:", signature)

    try:
        handler.handle(body, signature)
    except Exception as e:
        print("❌ ERROR:", e)
        return 'ERROR', 400

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text

    if msg == "桃園一日遊":
        flex_message = {
            "type": "bubble",
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "text",
                        "text": "桃園一日遊推薦景點",
                        "weight": "bold",
                        "size": "lg"
                    },
                    {
                        "type": "button",
                        "style": "primary",
                        "action": {
                            "type": "uri",
                            "label": "大溪老街",
                            "uri": "https://www.travel.taipei/zh-tw/attraction/details/440"
                        }
                    },
                    {
                        "type": "button",
                        "style": "primary",
                        "action": {
                            "type": "uri",
                            "label": "小烏來天空步道",
                            "uri": "https://www.travel.taipei/zh-tw/attraction/details/446"
                        }
                    }
                ]
            }
        }

        line_bot_api.reply_message(
            event.reply_token,
            FlexSendMessage(
                alt_text="桃園一日遊",
                contents=flex_message
            )
        )
    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=f"你說的是: {msg}")
        )

if __name__ == "__main__":
    # 讓 Heroku 自動抓 PORT
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)