import os
import requests
from linebot import LineBotApi
from linebot.exceptions import LineBotApiError
import json, dotenv

dotenv.load_dotenv()

#請在你的env中準備好 LINE_BOT_API_TOKEN

line_bot_api = LineBotApi(os.getenv('LINE_BOT_API_TOKEN'))
#請注意在創建時所選的json_menu_id所對應的image
def create_menu(json_menu_id, image_path)->str:#創建menu格式,(json格式id, path/to/your/image)
    headers = {
        "Authorization": "Bearer " + os.getenv('LINE_BOT_API_TOKEN'),
        "Content-Type": "application/json"
    }
    with open('rich_menu_config.json', 'r', encoding='utf-8') as json_file:
        menu_data = json.load(json_file)

    for body in menu_data:
        if body.get('id') == json_menu_id:
            break 
        else:
            print("json format error")
            return "json format error"

    req = requests.post('https://api.line.me/v2/bot/richmenu', headers=headers, json=body)

    if req.status_code == 200:
        response_data = req.json()
        rich_menu_id = response_data.get('richMenuId')
        try:                                          
            with open(image_path, 'rb') as f:
                line_bot_api.set_rich_menu_image(rich_menu_id, 'image/png', f)
                print(f"表單創建成功ID為:{rich_menu_id}，圖片上傳成功")
                return (f"表單創建成功ID為:{rich_menu_id}，圖片上傳成功")
        except LineBotApiError as e:
                print(f"圖片上傳失敗，錯誤訊息：{e}")
                return (f"圖片上傳失敗，錯誤訊息：{e}")
    else:
        print(f"表單創建失败，HTTP響應代碼為:{req.status_code}", req.text)
        return (f"表單創建失败，HTTP響應代碼為:{req.status_code}", req.text)
    
def delete_menu(rich_menu_id) -> str:
    try:
        line_bot_api.delete_rich_menu(rich_menu_id)
        print(f"成功刪除富文本菜單，ID為:{rich_menu_id}")
        return (f"成功刪除富文本菜單，ID為:{rich_menu_id}")
    except Exception as e:
        print(f"刪除富文本菜單時發生錯誤：{e}")
        return (f"刪除富文本菜單失敗，錯誤訊息：{e}")

#userID為個別使用者ID，要測試就用自己的ID
#以下menuID請換成你要的menu的ID
def switch__to_professor_menu(userID,professor_menu_ID):
    line_bot_api.link_rich_menu_to_user(userID,professor_menu_ID)

def switch_to_initial_menu(userID,initial_menu_ID):
    line_bot_api.link_rich_menu_to_user(userID,initial_menu_ID)

def switch_to_student_menu(userID,student_menu_ID):
    line_bot_api.link_rich_menu_to_user(userID,student_menu_ID)
