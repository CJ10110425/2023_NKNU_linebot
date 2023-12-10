
'''
使用linebot卻沒有初始化
'''

from MongoDB import activated_DB as act_DB
from MongoDB import temporary_DB as temp_DB
from MongoDB.professors_DB import professor_DB as prof_DB
from MongoDB.students_DB import student_DB as stu_DB
from Rich_menu import rich_menu
import logging as log


class visitor:
    def __init__(self, linebot) -> None:
        self.linebot = linebot
        self.if_msg_start_initializing()

    def if_msg_start_initializing(self) -> None:
        if self.linebot.msg.lower() == "start initializing" and self.linebot.status == 'standard':
            self.linebot.update_status("initializing")
            self.initializing()
        elif self.linebot.status == "initializing":
            self.initializing()
        else:
            rich_menu.switch_menu(self.linebot.id, "INITIAL_MENU_ID")
            self.linebot.reply_msg("請按下初始化按鈕")

    def change_level(self, level) -> None:
        '''
        更改level
        '''
        act_DB.update_level(self.linebot.id, level)

    def initializing(self) -> None:
        '''
        初始化功能
        '''
        level = self.linebot.level

        match level:
            case 0:
                temp_DB.insert_profile(
                    self.linebot.id, "none", "none", "none", "none")
                self.change_level(level + 1)
                self.linebot.reply_msg("請問你是？\n（學生/教授）\n請輸入（學生 or 教授）")
            case 1:
                temp_DB.update_identity(self.linebot.id, self.linebot.msg)
                self.change_level(level + 1)
                self.linebot.reply_msg("請輸入姓名")
            case 2:
                temp_DB.update_name(self.linebot.id, self.linebot.msg)
                self.change_level(level + 1)
                self.linebot.reply_msg("請輸入學校信箱")
            case 3:
                temp_DB.update_mail(self.linebot.id, self.linebot.msg)
                flag, activation_code = self.check_info_correct()
                if flag:
                    self.linebot.push_msg("正在核對您的資料...")
                    self.linebot.send_activation_email(
                        self.linebot.msg, activation_code)
                    self.change_level(level + 1)
                    self.linebot.reply_msg("請輸入啟動碼\n(已將啟動碼傳送到你的信箱\n稍等10秒)")
            case 4:
                if self.check_activation_code():
                    identity = temp_DB.find_identity(self.linebot.id)
                    temp_DB.delete_profile(self.linebot.id)
                    act_DB.update_all_to_none(self.linebot.id)
                    if identity["identity"] == "學生":
                        act_DB.update_identity(self.linebot.id,"學生")
                        rich_menu.switch_menu(
                            self.linebot.id, "STUDENT_MENU_ID")
                    elif identity["identity"] == "教授":
                        act_DB.update_identity(self.linebot.id,"教授")
                        rich_menu.switch_menu(
                            self.linebot.id, "PROFESSOR_MENU_ID")
                    else:
                        log.error("rich_menu error")
                    self.linebot.reply_msg("初始化完成\n請查看選單")

    def check_info_correct(self) -> bool:
        '''
        檢查資料是否正確
        '''
        profile = temp_DB.find_profile(self.linebot.id)
        if profile["identity"] == "學生":
            student = stu_DB.find_student_by_userid(self.linebot.id)
            if profile["name"] != student["stu_name"]:
                self.reset_profile()
                self.linebot.reply_msg("姓名 資料有誤，請重新輸入")
                return False,
            elif profile["mail"] != student["mail"]:
                self.reset_profile()
                self.linebot.reply_msg("mail 資料有誤，請重新輸入")
                return False,-1
            else:
                temp_DB.update_activation_code(
                    self.linebot.id, student["activation_code"])
                return True, student["activation_code"]
        elif profile["identity"] == "教授":
            professor = prof_DB.find_professor_by_userid(self.linebot.id)
            if profile["name"] != professor["pro_name"]:
                self.reset_profile()
                self.linebot.reply_msg("姓名 資料有誤，請重新輸入")
                return False
            elif profile["mail"] != professor["mail"]:
                self.reset_profile()
                self.linebot.reply_msg("mail 資料有誤，請重新輸入")
                return False
            else:
                temp_DB.update_activation_code(
                    self.linebot.id, professor["activation_code"])
                return True, professor["activation_code"]
        else:
            self.reset_profile()
            self.linebot.reply_msg("資料有誤，請重新輸入")
            return False,-1

    def check_activation_code(self) -> bool:
        '''
        檢查啟動碼是否正確
        '''
        profile = temp_DB.find_profile(self.linebot.id)
        activation_code = profile["activation_code"]
        if activation_code == self.linebot.msg:
            return True
        else:
            self.reset_profile()
            self.linebot.reply_msg("啟動碼有誤，請重新初始化")
            return False

    def reset_profile(self) -> None:
        '''
        重置資料
        '''
        temp_DB.delete_profile(self.linebot.id)
        act_DB.update_all_to_none(self.linebot.id)
