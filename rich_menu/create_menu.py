import os
import requests
from linebot import LineBotApi
from linebot.exceptions import LineBotApiError
import json
import dotenv

dotenv.load_dotenv()

# 請在你的env中準備好 line_bot_api_token

line_bot_api = LineBotApi(os.getenv('LINE_BOT_API_TOKEN'))


def create_rich_menu(headers, body, image_path) -> None:
    req = requests.post('https://api.line.me/v2/bot/richmenu',
                        headers=headers, json=body)

    if req.status_code == 200:
        response_data = req.json()
        rich_menu_id = response_data.get('richMenuId')

        try:
            with open(image_path, 'rb') as f:
                line_bot_api.set_rich_menu_image(rich_menu_id, 'image/png', f)
            return (f"圖片上傳成功\n表單創建成功，ID為 {rich_menu_id}")
        except LineBotApiError as e:
            print(f"圖片上傳失敗，錯誤訊息：{e}")
    else:
        print(f"表單創建失败，HTTP響應代碼為 {req.status_code}")
        print(req.text)



def create_menu_from_json(rich_menu_config, image_path, json_menu_id):
    with open(rich_menu_config, 'r', encoding='utf-8') as json_file:
        menu_data = json.load(json_file)

    headers = {
        "Authorization": "Bearer " + os.getenv('line_bot_api_token'),
        "Content-Type": "application/json"
    }

    for menu in menu_data:
        if menu.get('id') == json_menu_id:
            create_rich_menu(headers, menu, image_path)
            break


'''
    FIXME remember to change your image path
'''


def create_initial_menu():  # 創建初始menu,其中,路徑記得改
    create_menu_from_json('rich_menu_config.json',
                          'path/to/your/initial_image.jpg(png)', "initial_menu")


def create_professor_menu():  # 創建教授menu,其中,路徑記得改
    create_menu_from_json('rich_menu_config.json',
                          'path/to/your/professor_image.jpg(png)', "professor_menu")


# userID為個別使用者ID，要測試就用自己的ID
# 以下menuID請換成你要的menu的ID
def switch__to_professor_menu(userID, professor_menuID):
    line_bot_api.link_rich_menu_to_user(userID, professor_menuID)


def switch_to_initial_menu(userID, initial_menuID):
    line_bot_api.link_rich_menu_to_user(userID, initial_menuID)


def switch_to_student_menu(userID, student_menuID):
    line_bot_api.link_rich_menu_to_user(userID, student_menuID)
