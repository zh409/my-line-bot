from flask import Flask, request
from linebot import LineBotApi, WebhookHandler
from linebot.models import *
import os

app = Flask(__name__)

# LINE 金鑰（Render 環境變數）
LINE_CHANNEL_ACCESS_TOKEN = os.environ.get("LINE_CHANNEL_ACCESS_TOKEN")
LINE_CHANNEL_SECRET = os.environ.get("LINE_CHANNEL_SECRET")

line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(LINE_CHANNEL_SECRET)

# 首頁
@app.route("/")
def home():
    return "Senior Travel LINE Bot Running!"

# LINE Webhook
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers.get('X-Line-Signature')
    body = request.get_data(as_text=True)

    try:
        handler.handle(body, signature)
    except Exception as e:
        print("ERROR:", e)
        return 'ERROR', 400

    return 'OK'

# 訊息處理
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text

    # 銀髮族旅遊行程
    if msg in ["桃園銀髮一日遊", "銀髮旅遊", "桃園一日遊"]:

        flex_message = {
            "type": "carousel",
            "contents": [

                # 第一張：旅程介紹
                {
                    "type": "bubble",
                    "hero": {
                        "type": "image",
                        "url": "https://images.unsplash.com/photo-1506744038136-46273834b3fb",
                        "size": "full",
                        "aspectRatio": "20:13",
                        "aspectMode": "cover"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": "桃園銀髮慢活之旅",
                                "weight": "bold",
                                "size": "xl"
                            },
                            {
                                "type": "text",
                                "text": "專為銀髮族打造的無障礙慢活旅程，行程節奏寬鬆，提供專業陪同與多語言服務，讓長輩能安心享受與家人的旅行時光。",
                                "wrap": True,
                                "margin": "md",
                                "size": "sm"
                            }
                        ]
                    }
                },

                # 第二張：石門水庫
                {
                    "type": "bubble",
                    "hero": {
                        "type": "image",
                        "url": "https://travel.tycg.gov.tw/content/images/theme-tour/theme-w800-shihmen-12.jpg",
                        "size": "full",
                        "aspectRatio": "20:13",
                        "aspectMode": "cover"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": "石門水庫",
                                "weight": "bold",
                                "size": "lg"
                            },
                            {
                                "type": "text",
                                "text": "壩頂散步、欣賞湖景，步道平穩，非常適合長輩慢慢散心。",
                                "wrap": True,
                                "size": "sm",
                                "margin": "md"
                            },
                            {
                                "type": "text",
                                "text": "09:45 - 11:15",
                                "color": "#888888",
                                "size": "sm"
                            }
                        ]
                    }
                },

                # 第三張：月眉人工濕地
                {
                    "type": "bubble",
                    "hero": {
                        "type": "image",
                        "url": "https://tse4.mm.bing.net/th/id/OIP.oM_xBZCkpeFBELRTH8nRUQHaE8?r=0&rs=1&pid=ImgDetMain&o=7&rm=3",
                        "size": "full",
                        "aspectRatio": "20:13",
                        "aspectMode": "cover"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": "月眉人工濕地",
                                "weight": "bold",
                                "size": "lg"
                            },
                            {
                                "type": "text",
                                "text": "悠閒漫步落羽松大道，感受自然生態與寧靜風景。",
                                "wrap": True,
                                "size": "sm",
                                "margin": "md"
                            },
                            {
                                "type": "text",
                                "text": "11:30 - 12:45",
                                "color": "#888888",
                                "size": "sm"
                            }
                        ]
                    }
                },

                # 第四張：大溪老街
                {
                    "type": "bubble",
                    "hero": {
                        "type": "image",
                        "url": "https://tse1.mm.bing.net/th/id/OIP.2Ih1zR4bYHAfZs7LxxLBcwHaE8?r=0&rs=1&pid=ImgDetMain&o=7&rm=3",
                        "size": "full",
                        "aspectRatio": "20:13",
                        "aspectMode": "cover"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": "大溪老街",
                                "weight": "bold",
                                "size": "lg"
                            },
                            {
                                "type": "text",
                                "text": "品嚐在地美食，欣賞巴洛克式建築，安排舒適午餐時間。",
                                "wrap": True,
                                "size": "sm",
                                "margin": "md"
                            },
                            {
                                "type": "text",
                                "text": "13:00 - 14:30",
                                "color": "#888888",
                                "size": "sm"
                            }
                        ]
                    }
                },
                {
                        "type": "bubble",
                        "hero": {
                            "type": "image",
                            "url": "https://www.travel.tycg.gov.tw/content/images/attractions/73928/1024x768_attractions-image-wm9x7ra.jpg",
                            "size": "full",
                            "aspectRatio": "20:13",
                            "aspectMode": "cover"
                        },
                        "body": {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "虎頭山公園",
                                    "weight": "bold",
                                    "size": "lg"
                                },
                                {
                                    "type": "text",
                                    "text": "桃園知名森林公園，空氣清新、綠意盎然，適合長輩慢步放鬆，感受自然芬多精。",
                                    "wrap": True,
                                    "size": "sm",
                                    "margin": "md"
                                },
                                {
                                    "type": "text",
                                    "text": "15:00 - 16:45",
                                    "color": "#888888",
                                    "size": "sm"
                                }
                            ]
                        }
                    },
                      {
                        "type": "bubble",
                                    "hero": {
                                        "type": "image",
                                        "url": "https://www.travel.tycg.gov.tw/content/images/attractions/86327/1024x768_attractions-image-h9l7v2m.jpg",
                                        "size": "full",
                                        "aspectRatio": "20:13",
                                        "aspectMode": "cover"
                                    },
                                    "body": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "桃園觀光夜市",
                                                "weight": "bold",
                                                "size": "lg"
                                            },
                                            {
                                                "type": "text",
                                                "text": "享用在地特色晚餐與夜市小吃，體驗桃園熱鬧夜生活與台灣美食文化。",
                                                "wrap": True,
                                                "size": "sm",
                                                "margin": "md"
                                            },
                                            {
                                                "type": "text",
                                                "text": "17:15 - 18:30",
                                                "color": "#888888",
                                                "size": "sm"
                                            }
                                        ]
                                    }
                                },
                # 第五張：價格方案
                {
                    "type": "bubble",
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [

                            {
                                "type": "text",
                                "text": "旅遊價格方案",
                                "weight": "bold",
                                "size": "xl"
                            },

                            {
                                "type": "separator",
                                "margin": "md"
                            },

                            {
                                "type": "text",
                                "text": "平日價",
                                "weight": "bold",
                                "margin": "md"
                            },
                            {
                                "type": "text",
                                "text": "單人：$1,399",
                                "size": "sm"
                            },
                            {
                                "type": "text",
                                "text": "雙人：$1,259 /人",
                                "size": "sm"
                            },

                            {
                                "type": "separator",
                                "margin": "md"
                            },

                            {
                                "type": "text",
                                "text": "假日價",
                                "weight": "bold",
                                "margin": "md"
                            },
                            {
                                "type": "text",
                                "text": "單人：$1,499",
                                "size": "sm"
                            },
                            {
                                "type": "text",
                                "text": "雙人：$1,349 /人",
                                "size": "sm"
                            },

                            {
                                "type": "separator",
                                "margin": "md"
                            },

                            {
                                "type": "text",
                                "text": "企業包車",
                                "weight": "bold",
                                "margin": "md"
                            },
                            {
                                "type": "text",
                                "text": "$13,000（30人大巴）",
                                "size": "sm"
                            },

                            {
                                "type": "text",
                                "text": "原價 $1,999",
                                "size": "xs",
                                "color": "#999999",
                                "margin": "md"
                            }
                        ]
                    }
                }
            ]
        }
        

        line_bot_api.reply_message(
            event.reply_token,
            FlexSendMessage(
                alt_text="桃園銀髮慢活之旅",
                contents=flex_message
            )
        )

    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(
                text="請輸入「桃園銀髮一日遊」查看完整旅遊行程。"
            )
        )

# Render 用
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
