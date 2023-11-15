'''
    students functions
    1.organize_event
    2.ask_pro_question
'''

import os
from dotenv import load_dotenv
import openai


class student:
    def __init__(self, linebot) -> None:
        load_dotenv()
        self.linebot = linebot
        self.openai_key = os.getenv('OPENAI_KEY')
        openai.api_key = self.openai_key
        self.reply_msg = ""

    def student_function(self) -> None:
        Status = self.linebot.Status.lower()
        match Status:
            case "standard":
                self.determine_function()
            case "organize_event":
                self.organize_event()
            case "ask_pro_question":
                self.ask_pro_question()
            case _:
                self.reply_msg = "sorry, I don't understand"

    def determine_function(self) -> None:
        match self.linebot.msg:
            case "organize_event":
                self.linebot.Change_Status("organize_event")
                self.organize_event()
            case "ask_pro_question":
                self.linebot.Change_Status("ask_pro_question")
                self.ask_pro_question()
            case _:
                self.reply_msg = "sorry, I don't understand"
                self.linebot.reply_msg(self.reply_msg)
    
    def organize_event_level(self) -> int:
        '''
            to check msg user inputed correctness
            TODO: write logic
        '''

        msg = str(self.linebot.msg)
        level = self.linebot.Level
        match level:
            case "1":
                return 1
            case "2":
                return 2
            case "3":
                return 3
            case _:
                self.reply_msg = "sorry, I don't understand"
                self.linebot.reply_msg(self.reply_msg)
                return 0
    def organize_event(self) -> None:
        '''
            TODO: write logic
        '''


        level = self.organize_event_level()
        match level:
            case 0:
                return
            case _:
                self.reply_msg = "sorry, I don't understand"
                self.linebot.reply_msg(self.reply_msg)
                return
            
    def ask_pro_question_level(self) -> int:
        '''
            to check msg user inputed correctness
            TODO: write logic
        '''

        msg = str(self.linebot.msg)
        level = self.linebot.Level
        match level:
            case "1":
                return 1
            case "2":
                return 2
            case "3":
                return 3
            case _:
                self.reply_msg = "sorry, I don't understand"
                self.linebot.reply_msg(self.reply_msg)
                return 0
            
    def ask_pro_question(self) -> None:
        '''
            TODO: write logic
        '''


        level = self.ask_pro_question_level()
        match level:
            case 0:
                return
            case _:
                self.reply_msg = "sorry, I don't understand"
                self.linebot.reply_msg(self.reply_msg)
                return