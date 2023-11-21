'''
    students functions
    1.initiate_activity
    2.query_exam_info
    3.query_homework-info
    4.view_latest_activities
'''

import os
from dotenv import load_dotenv
import openai
import logging


class student:
    def __init__(self, linebot) -> None:
        load_dotenv()
        self.linebot = linebot
        self.openai_key = os.getenv('OPENAI_KEY')
        openai.api_key = self.openai_key
        self.reply_msg = ""

    def student_function(self) -> None:
        status = self.linebot.Status.lower()
        match status:
            case "standard":
                pass
            case "initiate_activity":
                self.initiate_activity()
            case "query_exam_info":
                self.query_exam_info()
            case "query_homework_info":
                self.query_homework_info()
            case "view_latest_activities":
                self.view_latest_activities()
            case _:
                logging.error(
                    'Unhandled case in professor_function with Status: %s', status)
                self.linebot.reply_msg(
                    'An unexpected error occurred. Please try again.g'
                )

    def determine_function(self) -> None:
        match self.linebot.msg:
            case "initiate activity":
                self.linebot.Change_Status("initiate_activity")
                self.initiate_activity()
            case "query exam info":
                self.linebot.Change_Status("query_exam_info")
                self.query_exam_info()
            case "query homework info":
                self.linebot.Change_Status("query_homework_info")
                self.query_homework_info()
            case "view latest activities":
                self.linebot.Change_Status("view_latest_activities")
                self.view_latest_activities()
            case _:
                logging.error(
                    'Unhandled case in determine_function with msg: %s', self.linebot.msg)
                self.linebot.reply_msg(
                    'An unexpected error occurred. Please try again.g'
                    )
    
    def initiate_activity_level(self) -> int:
        '''
        To check msg user inpted correctness
        '''

        msg = str(self.linebot.msg)
        level = self.linebot.Level
        match level:
            case 0:
                if msg == "initiate activity":
                    return level
                else:
                    '''
                    TODO: create a GPTs fine-tune model
                    '''

        
