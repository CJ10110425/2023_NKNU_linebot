import dotenv
from Rich_menu import rich_menu
dotenv.load_dotenv()

'''
    Create Init Database
'''


class _None:

    def __init__(self, linebot) -> None:
        self.linebot = linebot
        self.Identity = ["Professor", "Student"]
        self.Students = ["1"]  # TODO:Create Students table (DB)
        self.Professors = ["1"]  # TODO:Create Students table (DB)
        self.Register = "123321"  # self.linebot.Register FIXME: Can delete

    def Init(self):
        msg = self.linebot.msg
        match self.linebot.Status:
            case "Standard":
                '''Choose Identity'''

                match msg:
                    case "Student":
                        '''jump to Student function'''
                        self.linebot.Change_Status("Student_Init")
                        self.Student_Init()
                    case "Professor":
                        self.linebot.Change_Status('Professor_Init')
                        self.Professor_Init()
                    case _:
                        rich_menu.switch_menu(
                            self.linebot.ID, "INITIAL_MENU_ID")
                        self.linebot.reply_msg(
                            "Choose your Identity (Professor / Student)")
            case "Student_Init":
                '''jump to Student function'''
                self.Student_Init()
            case "Professor_Init":
                '''jump to Professor function'''
                self.Professor_Init()

    def Student_Level(self) -> int:
        '''
            To check msg user inputed correctness
            if it correct jump into next Level ,otherwiise it will jump into currrent Level
        '''

        msg = self.linebot.msg
        match self.linebot.Level:
            case 0:
                for num in self.Students:
                    if num == msg:
                        return self.linebot.Level + 1
                '''
                    Query DB with Students number and find and store AC 
                    self.linebot.Change_Register(AC)
                '''
            case 1:
                if self.Register == msg:
                    return self.linebot.Level + 1
                else:
                    return -1
            case _:
                print("Error")
        return self.linebot.Level

    def Student_Init(self) -> None:

        Level = self.Student_Level()  # To confirm msg is correct

        match Level:
            case 0:
                self.linebot.Change_Level(Level)
                self.linebot.reply_msg("Choose your Identity number")
            case 1:
                self.linebot.Change_Level(Level)
                self.linebot.reply_msg("Input your Activation Code")
            case 2:
                self.linebot.Change_Identity("Student")
                self.linebot.Change_Status("Standard")
                self.linebot.Change_Level(0)
                Data = " *** Query Database with Identity to findout Profile"
                rich_menu.switch_menu(self.linebot.ID, "STUDENT_MENU_ID")
                self.linebot.reply_msg(
                    Data+"\n Initialization successful\nPlease restart your line app")
            case _:
                self.linebot.Change_Status("Standard")
                self.linebot.Change_Level(0)
                self.linebot.reply_msg("Error\nPlease reinitialize")

    def Professor_Level(self) -> int:
        '''
            To check msg user inputed correctness
            if it correct jump into next Level ,otherwiise it will jump into currrent Level
        '''

        msg = self.linebot.msg
        match self.linebot.Level:
            case 0:
                for num in self.Professors:
                    if num == msg:
                        return 1
                '''
                    Query DB with Students number and find and store AC 
                    self.linebot.Change_Register(AC)
                '''
            case 1:
                if self.Register == msg:
                    return 2
                else:
                    return -1
            case _:
                print("Error")
        return self.linebot.Level

    def Professor_Init(self) -> None:
        Level = self.Professor_Level()  # To confirm msg is correct

        match Level:
            case 0:
                self.linebot.Change_Level(Level)
                self.linebot.reply_msg("Choose your Identity number")
            case 1:
                self.linebot.Change_Level(Level)
                self.linebot.reply_msg("Input your Activation Code")
            case 2:
                self.linebot.Change_Identity("Professor")
                self.linebot.Change_Status("Standard")
                self.linebot.Change_Level(0)
                Data = " *** Query Database with Identity to findout Profile"
                rich_menu.switch_menu(self.linebot.ID, "PROFESSOR_MENU_ID")
                self.linebot.reply_msg(
                    Data+"\n Initialization successful\nPlease restart your line app")
            case _:
                self.linebot.Change_Status("Standard")
                self.linebot.Change_Level(0)
                self.linebot.reply_msg("Error\nPlease reinitialize")

    # def Check_and_Change_Status(self) -> None:
    #     msg=self.linebot.msg
    #     match self.linebot.Status:
    #         case "Standard":
    #             '''Choose Identity'''
    #             if re.match("Student",msg):
    #                 self.linebot.Change_Status("Student_Init_1")
    #             elif re.match ("Professor",msg):
    #                 self.linebot.Change_Status('Professor_Init_1')
    #         case "Professor_Init_1":
    #             '''Choose Number'''
    #             for condition in self.Init_2:
    #                 if re.match(condition,msg):
    #                     self.linebot.Change_Status("Professor_Init_2")
    #                     break

    #         case "Professor_Init_2":
    #             '''Input activation code'''
    #             if re.match(self.Init_3,msg):
    #                 self.linebot.Change_Status("Professor_Init_3")
    #             else:
    #                 '''
    #                     Jump to Standard and Reinitialize
    #                 '''
    #                 self.linebot.Change_Status("Standard")
    #                 self.linebot.reply_msg("Error msg\nChoose your Identity again")

    #         case "Student_Init_1":
    #             '''Choose Number'''
    #             for condition in self.Init_2:
    #                 if re.match(condition,msg):
    #                     self.linebot.Change_Status("Student_Init_2")
    #                     break

    #         case "Student_Init_2":
    #             '''Input activation code'''
    #             if re.match(self.Init_3,msg):
    #                 self.linebot.Change_Status("Student_Init_3")
    #             else:
    #                 '''
    #                     Jump to Standard and Reinitialize
    #                 '''
    #                 self.linebot.Change_Status("Standard")
    #                 self.linebot.reply_msg("Error msg\nChoose your Identity again\nChoose your Identity (Professor / Student)")

    #         case _:
    #             '''No change Status'''
    #             self.linebot.push_msg("Please enter correct msg")

    # def Find_Professor_AC(self) -> int:
    #     '''User for Loop to search Professor DB and return Professor Activaation Code '''
    #     Code="*** Find function"
    #     return Code

    # def initialize(self) -> None:
    #     self.Check_and_Change_Status()
    #     Status=self.linebot.Status

    #     if Status == "Standard":
    #         # If the AC is incorrect ,a bug will occur
    #         #Bug : "POST /callback HTTP/1.1" 500 -,exceeded number of replies
    #         self.linebot.reply_msg("Choose your Identity (Professor / Student)")

    #     elif Status == "Professor_Init_1":
    #         '''
    #             Input: Identity (Professor / Student)
    #         '''

    #     elif Status == "Professor_Init_2":
    #         '''
    #             Input: Number (1 ... ?)
    #         '''
    #         Data=" *** Query Database with Identity"

    #         " *** Query Database with Identity to find out AC"
    #         self.linebot.Change_Register("123321")

    #         self.linebot.reply_msg(Data+"\nInput your Activation Code" )

    #     elif Status == "Professor_Init_3":
    #         '''
    #             Input: Activation Code (such as "123321")
    #         '''

    #         '''
    #             *** switch rich menu to Professor menu
    #         '''

    #         '''
    #         Maybe wa can change Status from Professor_Init_3 to Standard
    #         '''

    #         self.linebot.Change_Identity("Professor")
    #         self.linebot.Change_Status("Standard")
    #         Data=" *** Query Database with Identity to findout Profile"
    #         self.linebot.reply_msg(Data+"\n Initialization successful\nPlease restart your line app" )

    #     elif Status == "Student_Init_1":
    #         '''
    #             Input: Identity (Professor / Student)
    #         '''
    #         Data=" *** Query Student Database with Identity"
    #         self.linebot.reply_msg("Choose your Number" + Data)

    #     elif Status == "Student_Init_2":
    #         '''
    #             Input: Number (1 ... ?)
    #         '''
    #         Data=" *** Query Database with Identity"

    #         " *** Query Database with Identity to find out AC"
    #         self.linebot.Change_Register("123456")

    #         self.linebot.reply_msg(Data+"\nInput your Activation Code" )

    #     elif Status == "Student_Init_3":
    #         '''
    #             Input: Activation Code (such as "123456")
    #         '''

    #         '''
    #             *** switch rich menu to Student menu
    #         '''

    #         self.linebot.Change_Identity("Student")
    #         self.linebot.Change_Status("Standard")
    #         Data=" *** Query Database with Identity to findout Profile"
    #         self.linebot.reply_msg(Data+"\n Initialization successful\nPlease restart your line app" )
