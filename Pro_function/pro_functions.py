'''
    professor functions
    1.distribute_homework
    2.announce_exam
    3.handle_student_question
'''
import os
import openai
import time
import logging
from Pro_function import pro_anno_exam
from dotenv import load_dotenv
import logging as log
import json


class professor:
    def __init__(self, linebot) -> None:
        load_dotenv()
        self.linebot = linebot
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        openai.api_key = self.openai_api_key
        self.reply_msg = ""
        self.professor_function()

    def read_json_rule() -> dict:
        file_path = 'Rule/rules.json'
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)

            rule_1_content = data.get("professors_rules", {})

            return rule_1_content
        except Exception as e:
            print("發生錯誤：", e)
            return "讀取教授規則錯誤"

    def professor_function(self) -> None:
        status = self.linebot.Status.lower()
        msg = self.linebot.msg
        match status:
            case "standard":
                match msg.lower():
                    case "distribute_homework":
                        self.linebot.update_status("distribute_homework")
                        self.distribute_homework()
                    case "announce_exam":
                        self.linebot.update_status("announce_exam")
                        self.announce_exam()
                    case "handle_student_question":
                        self.linebot.update_status("handle_student_question")
                        self.handle_student_question()
            case "distribute_homework":
                self.distribute_homework()
            case "announce_exam":
                self.announce_exam()
            case "handle_student_question":
                self.handle_student_question()
            case _:
                logging.error(
                    'Unhandled case in professor_function with Status: %s', status)
                self.linebot.reply_msg(
                    "An unexpected error occurred. Please try again.")

    def send_msg_to_students(self, msg: str, students_user_id_list) -> None:
        for student_user_id in students_user_id_list:
            self.linebot.push_msg(msg, student_user_id)

    def announce_exam_level(self) -> int:
        '''
            to check msg user inputed correctness
        '''

        msg = str(self.linebot.msg)
        level = self.linebot.Level
        match level:
            case 0:
                if msg.lower() == "announce_exam":
                    return level
                else:
                    self.reply_msg, flag = pro_anno_exam.Organising_Profes_test_text(
                        self.linebot.msg)
                    if flag:
                        return level + 1
                    else:
                        return level
            case 1:
                if msg.lower() == "ok":
                    return level + 1
                else:
                    return level - 1
            case _:
                logging.error(
                    'Unhandled case in announce_exam_level with level: %s', level)
                self.linebot.reply_msg(
                    "An unexpected error occurred. Please try again.")
                return level  # 或者返回一个代表错误状态的特殊值

    def announce_exam(self) -> None:
        '''TODO: create rule.json to set up the rule (read/write file)'''
        '''TODO: create get_rule.py to read rule.json'''
        level = self.announce_exam_level()
        match level:
            case 0:
                rule = self.read_json_rule()
                self.linebot.Change_Level(level)
                self.linebot.reply_msg(rule["annouce_exam"]["rule_1"]+self.reply_msg)
            case 1:
                self.linebot.Change_Level(level)
                self.linebot.reply_msg(
                    self.reply_msg+"\nplease confirm whether the text is correct (ok/no)")
            case 2:
                self.linebot.Change_Level(0)
                self.linebot.Change_Status("Standard")
                '''
                    TODO: send msg to student
                '''
                self.linebot.reply_msg(
                    "completed sending message to your students,thank you")

    def distribute_homework_level(self) -> int:
        '''
            to check msg user inputed correctness
        '''

        msg = str(self.linebot.msg)
        level = self.linebot.Level
        match level:
            case 0:
                if msg.lower() == "distribute_homework":
                    return level
                else:
                    self.reply_msg, flag = pro_anno_exam.Organising_Profes_test_text(  # TODO: create Pro_dist_work.Organising_Profes_test_text
                        self.linebot.msg)
            case 1:
                if msg.lower() == "ok":
                    return level + 1
                else:
                    return level - 1
            case _:
                logging.error(
                    'Unhandled case in announce_exam_level with level: %s', level)
                self.linebot.reply_msg(
                    "An unexpected error occurred. Please try again.")
                return level  # 或者返回一个代表错误状态的特殊值

    def distribute_homework(self) -> None:
        '''TODO: create rule.json to set up the rule (read/write file)'''
        '''TODO: create get_rule.py to read rule.json'''
        level = self.distribute_homework_level()
        match level:
            case 0:
                self.linebot.Change_Level(level)
                self.linebot.reply_msg("rule"+self.reply_msg)
            case 1:
                self.linebot.Change_Level(level)
                self.linebot.reply_msg(
                    self.reply_msg+"\nplease confirm whether the text is correct (ok/no)")
            case 2:
                self.linebot.Change_Level(0)
                self.linebot.Change_Status("Standard")
                '''
                    TODO: send msg to student
                '''
                self.linebot.reply_msg(
                    "completed sending message to your students,thank you")
                self.linebot.reply_msg(
                    "completed sending message to your students,thank you")

    def handle_student_question(self) -> None:
        '''
            use to handle student question
        '''
        pass
