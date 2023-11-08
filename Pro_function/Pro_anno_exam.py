import openai
import re
import os
from dotenv import load_dotenv


# Organize professor's copywriting
def Organising_Profes_test_text(msg) -> (str,bool):
    completion = openai.ChatCompletion.create(
        model="ft:gpt-3.5-turbo-0613:personal::8Hwz1kxq",
        messages=[{"role": "system", "content": "2023年,當一個高雄師範大學電子工程系教授的助理,幫教授整理文案並且遵照順序列出日期、時間、地點、科目、範圍（章）、是否開書考,只能回覆考試內容"}, {
            "role": "user", "content": msg}]
    )
    generated_text = completion['choices'][0]['message']['content']
    generated_text = stop_content(generated_text)
    generated_text,flag= extract_pending_info(generated_text)
    return generated_text,flag


# Filter pending items and remind users to complete them
def extract_pending_info(text) -> str:
    pattern = r'-(\s*\S+?)\s*：\s*待定'
    matches = re.findall(pattern, text)

    if matches:
        pending_items = '、'.join(matches).strip()
        return f"\n請完成『{pending_items}』項目",False
    elif is_hyphen_starting(text):
        return text,True
    else :
        return "\n"+text,False


# Stop_content function
def stop_content(text) -> str:
    stop_word = " END"
    if stop_word in text:
        generated_text = text.split(stop_word)[0].strip()
        return generated_text
    else:
        return text

# confirm hyphen starting
def is_hyphen_starting(input_str):
    if input_str.startswith('-'):
        return True
    else:
        return False



if __name__ == "__main__":
    # loading evn var
    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")
    msg = "上午11點到下午2點考物理第三章到第八章在512教室不開書考試"
    print(Organising_Profes_test_text(msg))
