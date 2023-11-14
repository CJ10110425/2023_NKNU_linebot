'''
    professor functions
    1.distribute_homework
    2.announce_exam
    3.handle_student_question
'''
import os
from dotenv import load_dotenv
import openai
import pro_anno_exam


class professor:
    def __init__(self, linebot) -> None:
        load_dotenv()
        self.linebot = linebot
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        openai.api_key = self.openai_api_key
        self.reply_msg = ""

    def professor_function(self) -> None:
        Status = self.linebot.Status.lower()
        match Status:
            case "standard":
                self.determine_function()
            case "distribute_homework":
                self.distribute_homework()
            case "announce_exam":
                self.announce_exam()
            case "handle_student_question":
                self.handle_student_question()

    def determine_function(self) -> None:
        match self.linebot.msg:
            case "distribute_homework":
                self.linebot.Change_Status("distribute_homework")
                self.distribute_homework()
            case "announce_exam":
                self.linebot.Change_Status("announce_exam")
                self.announce_exam()
            case "handle_student_question":
                self.linebot.Change_Status("handle_student_question")
                self.handle_student_question()

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
                    self.reply_msg, flag = Pro_anno_exam.Organising_Profes_test_text(
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
                print("error")

    def announce_exam(self) -> None:
        '''TODO: create rule.json to set up the rule (read/write file)'''
        '''TODO: create get_rule.py to read rule.json'''
        level = self.announce_exam_level()
        match level:
            case 0:
                self.linebot.Change_Level(level)
                # TODO: create rule.json to set up the rule (read/write file)
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
                    self.reply_msg, flag = Pro_anno_exam.Organising_Profes_test_text(  # TODO: create Pro_dist_work.Organising_Profes_test_text
                        self.linebot.msg)
            case 1:
                if msg.lower() == "ok":
                    return level + 1
                else:
                    return level - 1
            case _:
                print("error")

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
