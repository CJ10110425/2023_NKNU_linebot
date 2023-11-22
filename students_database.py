import students_functions
import pymongo
import dotenv
import os

dotenv.load_dotenv()

## 下面連結得自行連結 ##
myclient = pymongo.MongoClient(os.getenv("MONGODB_URL"))
mydb = myclient["student_db"]
mycol = mydb["student_profile"]

students_data = [
    {
        "user_id": "王麒勛",
        "stu_name": "王麒勛",
        "stu_gender": "male",
        "stu_id": "410974030",
        "stu_subject": [

            "Introduction to Microwave",
            "Microelectronics Circuits Experiment and Design(II)",
            "Physics of Semiconductor Devices",
            "Introduction to Optoelectronic",
            "Electronics(III)",
            "Microprocessor",
            "Digital System Design"
        ],
        "mail": "410974030@mail.nknu.edu.tw",
        "activation_code": "410974030",
        "status": "standard",
        "level": 0,
        "identity": "none"
    },
    {
        "user_id": "吳嘉芸",
        "stu_name": "吳嘉芸",
        "stu_gender": "female",
        "stu_id": "411072002",
        "stu_subject": [

            "Introduction to Microwave",
            "Microelectronics Circuits Experiment and Design(II)",
            "Physics of Semiconductor Devices",
            "Introduction to Optoelectronic",
            "Electronics(III)",
            "Microprocessor"
        ],
        "mail": "411072002@mail.nknu.edu.tw",
        "activation_code": "411072002",
        "status": "standard",
        "level": 0,
        "identity": "none"
    },
     {
        "user_id": "陳信宏",
        "stu_name": "陳信宏",
        "stu_gender": "male",
        "stu_id": "411071102",
        "stu_subject": [

            "Introduction to Microwave",
            "Microelectronics Circuits Experiment and Design(II)",
            "Physics of Semiconductor Devices",
            "Electronics(III)",
            "Digital System Design"
        ],
        "mail": "411071102@mail.nknu.edu.tw",
        "activation_code": "411071102",
        "status": "standard",
        "level": 0,
        "identity": "none"
    },
    {
        "user_id": "許晉嘉",
        "stu_name": "許晉嘉",
        "stu_gender": "male",
        "stu_id": "411074001",
        "stu_subject": [

            "Introduction to Microwave",
            "Microelectronics Circuits Experiment and Design(II)",
            "Physics of Semiconductor Devices",
            "Introduction to Optoelectronic",
            "Electronics(III)",
            "Microprocessor",
            "Digital System Design"
        ],
        "mail": "411074001@mail.nknu.edu.tw",
        "activation_code": "411074001",
        "status": "standard",
        "level": 0,
        "identity": "none"
    },
    {
        "user_id": "李定頤",
        "stu_name": "李定頤",
        "stu_gender": "male",
        "stu_id": "411074002",
        "stu_subject": [

            "Introduction to Microwave",
            "Microelectronics Circuits Experiment and Design(II)",
            "Physics of Semiconductor Devices",
            "Electronics(III)",
            "Microprocessor",
            "Digital System Design"
        ],
        "mail": "411074002@mail.nknu.edu.tw",
        "activation_code": "411074002",
        "status": "standard",
        "level": 0,
        "identity": "none"
    },
    {
        "user_id": "賴英儒",
        "stu_name": "賴英儒",
        "stu_gender": "male",
        "stu_id": "411074003",
        "stu_subject": [

            "Introduction to Microwave",
            "Microelectronics Circuits Experiment and Design(II)",
            "Physics of Semiconductor Devices",
            "Introduction to Optoelectronic",
            "Electronics(III)",
            "Microprocessor"
        ],
        "mail": "411074003@mail.nknu.edu.tw",
        "activation_code": "411074003",
        "status": "standard",
        "level": 0,
        "identity": "none"
    },
    {
        "user_id": "穆翊丞",
        "stu_name": "穆翊丞",
        "stu_gender": "male",
        "stu_id": "411074004",
        "stu_subject": [

            "Introduction to Microwave",
            "Microelectronics Circuits Experiment and Design(II)",
            "Physics of Semiconductor Devices",
            "Introduction to Optoelectronic",
            "Electronics(III)",
            "Microprocessor",
            "Digital System Design"
        ],
        "mail": "411074004@mail.nknu.edu.tw",
        "activation_code": "411074004",
        "status": "standard",
        "level": 0,
        "identity": "none"
    },
    {
        "user_id": "陳冠瑜",
        "stu_name": "陳冠瑜",
        "stu_gender": "female",
        "stu_id": "411074005",
        "stu_subject": [

            "Introduction to Microwave",
            "Microelectronics Circuits Experiment and Design(II)",
            "Physics of Semiconductor Devices",
            "Introduction to Optoelectronic",
            "Electronics(III)",
            "Microprocessor"
        ],
        "mail": "411074005@mail.nknu.edu.tw",
        "activation_code": "411074005",
        "status": "standard",
        "level": 0,
        "identity": "none"
    },
    {
        "user_id": "陳品豪",
        "stu_name": "陳品豪",
        "stu_gender": "male",
        "stu_id": "411074006",
        "stu_subject": [

            "Introduction to Microwave",
            "Microelectronics Circuits Experiment and Design(II)",
            "Physics of Semiconductor Devices",
            "Introduction to Optoelectronic",
            "Electronics(III)",
            "Digital System Design"
        ],
        "mail": "411074006@mail.nknu.edu.tw",
        "activation_code": "411074006",
        "status": "standard",
        "level": 0,
        "identity": "none"
    },
    {
        "user_id": "高子晴",
        "stu_name": "高子晴",
        "stu_gender": "female",
        "stu_id": "411074007",
        "stu_subject": [

            "Introduction to Microwave",
            "Microelectronics Circuits Experiment and Design(II)",
            "Physics of Semiconductor Devices",
            "Introduction to Optoelectronic",
            "Electronics(III)",
            "Microprocessor"
        ],
        "mail": "411074007@mail.nknu.edu.tw",
        "activation_code": "411074007",
        "status": "standard",
        "level": 0,
        "identity": "none"
    },
    {
        "user_id": "李品澤",
        "stu_name": "李品澤",
        "stu_gender": "male",
        "stu_id": "411074008",
        "stu_subject": [

            "Introduction to Microwave",
            "Microelectronics Circuits Experiment and Design(II)",
            "Physics of Semiconductor Devices",
            "Introduction to Optoelectronic",
            "Electronics(III)",
            "Microprocessor"
        ],
        "mail": "411074008@mail.nknu.edu.tw",
        "activation_code": "411074008",
        "status": "standard",
        "level": 0,
        "identity": "none"
    },
    {
        "user_id": "陳守歆",
        "stu_name": "陳守歆",
        "stu_gender": "male",
        "stu_id": "411074009",
        "stu_subject": [

            "Introduction to Microwave",
            "Microelectronics Circuits Experiment and Design(II)",
            "Physics of Semiconductor Devices",
            "Electronics(III)",
            "Microprocessor",
            "Digital System Design"
        ],
        "mail": "411074009@mail.nknu.edu.tw",
        "activation_code": "411074009",
        "status": "standard",
        "level": 0,
        "identity": "none"
    },
    {
        "user_id": "許鈞皓",
        "stu_name": "許鈞皓",
        "stu_gender": "male",
        "stu_id": "411074010",
        "stu_subject": [

            "Introduction to Microwave",
            "Microelectronics Circuits Experiment and Design(II)",
            "Physics of Semiconductor Devices",
            "Introduction to Optoelectronic",
            "Electronics(III)",
            "Microprocessor",
            "Digital System Design"
        ],
        "mail": "411074010@mail.nknu.edu.tw",
        "activation_code": "411074010",
        "status": "standard",
        "level": 0,
        "identity": "none"
    },
    {
        "user_id": "巫騏丞",
        "stu_name": "巫騏丞",
        "stu_gender": "male",
        "stu_id": "411074011",
        "stu_subject": [

            "Introduction to Microwave",
            "Microelectronics Circuits Experiment and Design(II)",
            "Physics of Semiconductor Devices",
            "Electronics(III)",
            "Microprocessor",
            "Digital System Design"
        ],
        "mail": "411074011@mail.nknu.edu.tw",
        "activation_code": "411074011",
        "status": "standard",
        "level": 0,
        "identity": "none"
    },
    {
        "user_id": "陳冠杰",
        "stu_name": "陳冠杰",
        "stu_gender": "male",
        "stu_id": "411074012",
        "stu_subject": [

            "Introduction to Microwave",
            "Microelectronics Circuits Experiment and Design(II)",
            "Physics of Semiconductor Devices",
            "Electronics(III)",
            "Microprocessor",
            "Digital System Design"
        ],
        "mail": "411074012@mail.nknu.edu.tw",
        "activation_code": "411074012",
        "status": "standard",
        "level": 0,
        "identity": "none"
    },
    {
        "user_id": "李翊宇",
        "stu_name": "李翊宇",
        "stu_gender": "male",
        "stu_id": "411074013",
        "stu_subject": [

            "Introduction to Microwave",
            "Microelectronics Circuits Experiment and Design(II)",
            "Physics of Semiconductor Devices",
            "Introduction to Optoelectronic",
            "Electronics(III)",
            "Microprocessor",
            "Digital System Design"
        ],
        "mail": "411074013@mail.nknu.edu.tw",
        "activation_code": "411074013",
        "status": "standard",
        "level": 0,
        "identity": "none"
    },
    {
        "user_id": "徐琬婷",
        "stu_name": "徐琬婷",
        "stu_gender": "female",
        "stu_id": "411074014",
        "stu_subject": [

            "Introduction to Microwave",
            "Microelectronics Circuits Experiment and Design(II)",
            "Physics of Semiconductor Devices",
            "Introduction to Optoelectronic",
            "Electronics(III)",
            "Microprocessor"
        ],
        "mail": "411074014@mail.nknu.edu.tw",
        "activation_code": "411074014",
        "status": "standard",
        "level": 0,
        "identity": "none"
    },
    {
        "user_id": "呂秉融",
        "stu_name": "呂秉融",
        "stu_gender": "male",
        "stu_id": "411074015",
        "stu_subject": [

            "Introduction to Microwave",
            "Microelectronics Circuits Experiment and Design(II)",
            "Physics of Semiconductor Devices",
            "Introduction to Optoelectronic",
            "Electronics(III)",
            "Microprocessor",
            "Digital System Design"
        ],
        "mail": "411074015@mail.nknu.edu.tw",
        "activation_code": "411074015",
        "status": "standard",
        "level": 0,
        "identity": "none"
    },
    {
        "user_id": "林育鋐",
        "stu_name": "林育鋐",
        "stu_gender": "male",
        "stu_id": "411074016",
        "stu_subject": [

            "Introduction to Microwave",
            "Microelectronics Circuits Experiment and Design(II)",
            "Physics of Semiconductor Devices",
            "Electronics(III)",
            "Microprocessor","Digital System Design"
            
            ],
        "mail": "411074016@mail.nknu.edu.tw",
        "activation_code": "411074016",
        "status": "standard",
        "level": 0,
        "identity": "none"
    },
    {
        "user_id": "楊薪樺",
        "stu_name": "楊薪樺",
        "stu_gender": "male",
        "stu_id": "411074017",
        "stu_subject": [
            
            "Introduction to Microwave",
            "Microelectronics Circuits Experiment and Design(II)",
            "Physics of Semiconductor Devices",
            "Introduction to Optoelectronic",
            "Electronics(III)",
            "Microprocessor",
            "Digital System Design"
            
            ],
        "mail": "411074017@mail.nknu.edu.tw",
        "activation_code": "411074017",
        "status": "standard",
        "level": 0,
        "identity": "none"
    },
    {
        "user_id": "李秉修",
        "stu_name": "李秉修",
        "stu_gender": "male",
        "stu_id": "411074018",
        "stu_subject": [
            
            "Introduction to Microwave",
            "Microelectronics Circuits Experiment and Design(II)", 
            "Physics of Semiconductor Devices", 
            "Introduction to Optoelectronic", 
            "Electronics(III)", 
            "Microprocessor"
            
            ],
        "mail": "411074018@mail.nknu.edu.tw",
        "activation_code": "411074018",
        "status": "standard",
        "level": 0,
        "identity": "none"
    },
    {
        "user_id": "張瑋庭",
        "stu_name": "張瑋庭",
        "stu_gender": "female",
        "stu_id": "411074019",
        "stu_subject": [
            
            "Introduction to Microwave", 
            "Microelectronics Circuits Experiment and Design(II)", 
            "Physics of Semiconductor Devices", 
            "Introduction to Optoelectronic", 
            "Electronics(III)", 
            "Microprocessor", 
            "Digital System Design"
            
            ],
        "mail": "411074019@mail.nknu.edu.tw",
        "activation_code": "411074019",
        "status": "standard",
        "level": 0,
        "identity": "none"
    },
    {
        "user_id": "鄭珮慈",
        "stu_name": "鄭珮慈",
        "stu_gender": "female",
        "stu_id": "411074020",
        "stu_subject": [
            
            "Introduction to Microwave", 
            "Microelectronics Circuits Experiment and Design(II)", 
            "Physics of Semiconductor Devices", 
            "Electronics(III)", 
            "Microprocessor", 
            "Digital System Design"
            
            ],
        "mail": "411074020@mail.nknu.edu.tw",
        "activation_code": "411074020",
        "status": "standard",
        "level": 0,
        "identity": "none"
    },
    {
        "user_id": "鄭翔遠",
        "stu_name": "鄭翔遠",
        "stu_gender": "male",
        "stu_id": "411074021",
        "stu_subject": [

            "Introduction to Microwave", 
            "Microelectronics Circuits Experiment and Design(II)", 
            "Physics of Semiconductor Devices", 
            "Introduction to Optoelectronic", 
            "Electronics(III)", 
            "Microprocessor", 
            "Digital System Design"
            
            ],
        "mail": "411074021@mail.nknu.edu.tw",
        "activation_code": "411074021",
        "status": "standard",
        "level": 0,
        "identity": "none"
    },
    {
        "user_id": "鄭傑升",
        "stu_name": "鄭傑升",
        "stu_gender": "male",
        "stu_id": "411074022",
        "stu_subject": [
            
            "Introduction to Microwave", 
            "Microelectronics Circuits Experiment and Design(II)", 
            "Physics of Semiconductor Devices", 
            "Electronics(III)", 
            "Microprocessor", 
            "Digital System Design"

            ],
        "mail": "411074022@mail.nknu.edu.tw",
        "activation_code": "411074022",
        "status": "standard",
        "level": 0,
        "identity": "none"
    },
    {
        "user_id": "盧弘政",
        "stu_name": "盧弘政",
        "stu_gender": "male",
        "stu_id": "411074023",
        "stu_subject": [
            
            "Introduction to Microwave", 
            "Microelectronics Circuits Experiment and Design(II)", 
            "Physics of Semiconductor Devices", 
            "Introduction to Optoelectronic", 
            "Electronics(III)", 
            "Microprocessor", 
            "Digital System Design"

            ],
        "mail": "411074023@mail.nknu.edu.tw",
        "activation_code": "411074023",
        "status": "standard",
        "level": 0,
        "identity": "none"
    },
    {
        "user_id": "陳詠維",
        "stu_name": "陳詠維",
        "stu_gender": "male",
        "stu_id": "411074024",
        "stu_subject": [

            "Introduction to Microwave", 
            "Microelectronics Circuits Experiment and Design(II)", 
            "Physics of Semiconductor Devices", 
            "Introduction to Optoelectronic", 
            "Electronics(III)", 
            "Digital System Design"

            ],
        "mail": "411074024@mail.nknu.edu.tw",
        "activation_code": "411074024",
        "status": "standard",
        "level": 0,
        "identity": "none"
    },
    {
        "user_id": "陳冠廷",
        "stu_name": "陳冠廷",
        "stu_gender": "male",
        "stu_id": "411074025",
        "stu_subject": [
            
            "Introduction to Microwave", 
            "Microelectronics Circuits Experiment and Design(II)",
            "Physics of Semiconductor Devices", 
            "Electronics(III)", 
            "Microprocessor", 
            "Digital System Design"

            ],
        "mail": "411074025@mail.nknu.edu.tw",
        "activation_code": "411074025",
        "status": "standard",
        "level": 0,
        "identity": "none"
    },
    {
        "user_id": "邱亭瑄",
        "stu_name": "邱亭瑄",
        "stu_gender": "female",
        "stu_id": "411074026",
        "stu_subject": [
            
            "Introduction to Microwave", 
            "Microelectronics Circuits Experiment and Design(II)", 
            "Physics of Semiconductor Devices",
            "Introduction to Optoelectronic", 
            "Electronics(III)", 
            "Microprocessor", 
            "Digital System Design"
            
            ],
        "mail": "411074026@mail.nknu.edu.tw",
        "activation_code": "411074026",
        "status": "standard",
        "level": 0,
        "identity": "none"
    },
    {
        "user_id": "黃梓家",
        "stu_name": "黃梓家",
        "stu_gender": "male",
        "stu_id": "411074027",
        "stu_subject": [
            
            "Introduction to Microwave", 
            "Microelectronics Circuits Experiment and Design(II)", 
            "Physics of Semiconductor Devices", 
            "Electronics(III)", 
            "Microprocessor", 
            "Digital System Design"
            
            ],
        "mail": "411074027@mail.nknu.edu.tw",
        "activation_code": "411074027",
        "status": "standard",
        "level": 0,
        "identity": "none"
    },
    {
        "user_id": "戴承亮",
        "stu_name": "戴承亮",
        "stu_gender": "male",
        "stu_id": "411074028",
        "stu_subject": [
            
            "Introduction to Microwave", 
            "Microelectronics Circuits Experiment and Design(II)", 
            "Physics of Semiconductor Devices", 
            "Introduction to Optoelectronic", 
            "Electronics(III)", 
            "Microprocessor"
            
            ],
        "mail": "411074028@mail.nknu.edu.tw",
        "activation_code": "411074028",
        "status": "standard",
        "level": 0,
        "identity": "none"
    },
    {
        "user_id": "鄭皓儀",
        "stu_name": "鄭皓儀",
        "stu_gender": "male",
        "stu_id": "411074029",
        "stu_subject": [

            "Introduction to Microwave", 
            "Microelectronics Circuits Experiment and Design(II)", 
            "Physics of Semiconductor Devices", 
            "Introduction to Optoelectronic", 
            "Electronics(III)", 
            "Microprocessor"
            
            ],
        "mail": "411074029@mail.nknu.edu.tw",
        "activation_code": "411074029",
        "status": "standard",
        "level": 0,
        "identity": "none"
    },
    {
        "user_id": "徐翊博",
        "stu_name": "徐翊博",
        "stu_gender": "male",
        "stu_id": "411074030",
        "stu_subject": [
            
            "Introduction to Microwave", 
            "Microelectronics Circuits Experiment and Design(II)", 
            "Physics of Semiconductor Devices", 
            "Electronics(III)", 
            "Microprocessor", 
            "Digital System Design"
            
            ],
        "mail": "411074030@mail.nknu.edu.tw",
        "activation_code": "411074030",
        "status": "standard",
        "level": 0,
        "identity": "none"
    },
    {
        "user_id": "陳叡昱",
        "stu_name": "陳叡昱",
        "stu_gender": "male",
        "stu_id": "411074031",
        "stu_subject": [

            "Introduction to Microwave", 
            "Microelectronics Circuits Experiment and Design(II)", 
            "Physics of Semiconductor Devices", 
            "Electronics(III)", 
            "Microprocessor", 
            "Digital System Design"
            
            ],
        "mail": "411074031@mail.nknu.edu.tw",
        "activation_code": "411074031",
        "status": "standard",
        "level": 0,
        "identity": "none"
    },
    {
        "user_id": "郭少棋",
        "stu_name": "郭少棋",
        "stu_gender": "male",
        "stu_id": "411074033",
        "stu_subject": [
            
            "Introduction to Microwave", 
            "Microelectronics Circuits Experiment and Design(II)", 
            "Physics of Semiconductor Devices", 
            "Electronics(III)", 
            "Microprocessor", 
            "Digital System Design"
            
            ],
        "mail": "411074033@mail.nknu.edu.tw",
        "activation_code": "411074033",
        "status": "standard",
        "level": 0,
        "identity": "none"
    },
    {
        "user_id": "林廷翰",
        "stu_name": "林廷翰",
        "stu_gender": "male",
        "stu_id": "411074034",
        "stu_subject": [

            "Introduction to Microwave", 
            "Microelectronics Circuits Experiment and Design(II)", 
            "Physics of Semiconductor Devices", 
            "Electronics(III)", 
            "Microprocessor", 
            "Digital System Design"
            
            ],
        "mail": "411074034@mail.nknu.edu.tw",
        "activation_code": "411074034",
        "status": "standard",
        "level": 0,
        "identity": "none"
    },
    {
        "user_id": "鄭仁皓",
        "stu_name": "鄭仁皓",
        "stu_gender": "male",
        "stu_id": "411074036",
        "stu_subject": [
            
            "Introduction to Microwave", 
            "Microelectronics Circuits Experiment and Design(II)", 
            "Physics of Semiconductor Devices", 
            "Introduction to Optoelectronic", 
            "Electronics(III)", 
            "Microprocessor", 
            "Digital System Design"
            
            ],
        "mail": "411074036@mail.nknu.edu.tw",
        "activation_code": "411074036",
        "status": "standard",
        "level": 0,
        "identity": "none"
    },
    {
        "user_id": "林育紝",
        "stu_name": "林育紝",
        "stu_gender": "male",
        "stu_id": "411074038",
        "stu_subject": [
            
            "Introduction to Microwave", 
            "Microelectronics Circuits Experiment and Design(II)", 
            "Physics of Semiconductor Devices", 
            "Electronics(III)", 
            "Microprocessor", 
            "Digital System Design"
            
            ],
        "mail": "411074038@mail.nknu.edu.tw",
        "activation_code": "411074038",
        "status": "standard",
        "level": 0,
        "identity": "none"
    },
    {
        "user_id": "吳承衡",
        "stu_name": "吳承衡",
        "stu_gender": "male",
        "stu_id": "411074040",
        "stu_subject": [
            
            "Introduction to Microwave", 
            "Microelectronics Circuits Experiment and Design(II)",
            "Physics of Semiconductor Devices", 
            "Introduction to Optoelectronic", 
            "Electronics(III)", 
            "Microprocessor"
            
            ],
        "mail": "411074040@mail.nknu.edu.tw",
        "activation_code": "411074040",
        "status": "standard",
        "level": 0,
        "identity": "none"
    },
    {
        "user_id": "莊詠琇",
        "stu_name": "莊詠琇",
        "stu_gender": "male",
        "stu_id": "411074041",
        "stu_subject": [
            
            "Introduction to Microwave", 
            "Microelectronics Circuits Experiment and Design(II)", 
            "Physics of Semiconductor Devices", 
            "Introduction to Optoelectronic", 
            "Electronics(III)", 
            "Microprocessor"
            
            ],
        "mail": "411074041@mail.nknu.edu.tw",
        "activation_code": "411074041",
        "status": "standard",
        "level": 0,
        "identity": "none"
    },
    {
        "user_id": "何冠宏",
        "stu_name": "何冠宏",
        "stu_gender": "male",
        "stu_id": "411074042",
        "stu_subject": [

            "Introduction to Microwave", 
            "Microelectronics Circuits Experiment and Design(II)", 
            "Physics of Semiconductor Devices", 
            "Introduction to Optoelectronic", 
            "Electronics(III)", 
            "Microprocessor", 
            "Digital System Design"
            
            ],
        "mail": "411074042@mail.nknu.edu.tw",
        "activation_code": "411074042",
        "status": "standard",
        "level": 0,
        "identity": "none"
    },
    {
        "user_id": "王翊庭",
        "stu_name": "王翊庭",
        "stu_gender": "male",
        "stu_id": "411074044",
        "stu_subject": [
            
            "Introduction to Microwave",
            "Microelectronics Circuits Experiment and Design(II)", 
            "Physics of Semiconductor Devices", 
            "Introduction to Optoelectronic", 
            "Electronics(III)", 
            "Digital System Design"
            
            ],
        "mail": "411074044@mail.nknu.edu.tw",
        "activation_code": "411074044",
        "status": "standard",
        "level": 0,
        "identity": "none"
    },
    {
        "user_id": "周雋",
        "stu_name": "周雋",
        "stu_gender": "male",
        "stu_id": "411074045",
        "stu_subject": [
            
            "Introduction to Optoelectronic", 
            "Electronics(III)", 
            "Microprocessor", 
            "Digital System Design"
            
            ],
        "mail": "411074045@mail.nknu.edu.tw",
        "activation_code": "411074045",
        "status": "standard",
        "level": 0,
        "identity": "none"
    },
     {
        "user_id": "羅豊凱",
        "stu_name": "羅豊凱",
        "stu_gender": "male",
        "stu_id": "411074046",
        "stu_subject": [
            
            "Introduction to Microwave", 
            "Microelectronics Circuits Experiment and Design(II)", 
            "Physics of Semiconductor Devices", 
            "Introduction to Optoelectronic", 
            "Electronics(III)", 
            "Microprocessor", 
            "Digital System Design"
            
            ],
        "mail": "411074046@mail.nknu.edu.tw",
        "activation_code": "411074046",
        "status": "standard",
        "level": 0,
        "identity": "none"
    },
    {
        "user_id": "陳昱方",
        "stu_name": "陳昱方",
        "stu_gender": "male",
        "stu_id": "411074047",
        "stu_subject": [
            
            "Introduction to Microwave", 
            "Microelectronics Circuits Experiment and Design(II)", 
            "Physics of Semiconductor Devices", 
            "Introduction to Optoelectronic", 
            "Electronics(III)", 
            "Microprocessor", 
            "Digital System Design"
            
            ],
        "mail": "411074047@mail.nknu.edu.tw",
        "activation_code": "411074047",
        "status": "standard",
        "level": 0,
        "identity": "none"
    },
    {
        "user_id": "王孟書",
        "stu_name": "王孟書",
        "stu_gender": "male",
        "stu_id": "411074048",
        "stu_subject": [
            
            "Introduction to Microwave", 
            "Microelectronics Circuits Experiment and Design(II)", 
            "Physics of Semiconductor Devices", 
            "Introduction to Optoelectronic", 
            "Electronics(III)", "Microprocessor", 
            "Digital System Design"
            
            ],
        "mail": "411074048@mail.nknu.edu.tw",
        "activation_code": "411074048",
        "status": "standard",
        "level": 0,
        "identity": "none"
    },
    {
        "user_id": "蔡碧陽",
        "stu_name": "蔡碧陽",
        "stu_gender": "male",
        "stu_id": "411074050",
        "stu_subject": [
            
            "Introduction to Microwave", 
            "Microelectronics Circuits Experiment and Design(II)", 
            "Physics of Semiconductor Devices", 
            "Introduction to Optoelectronic", 
            "Electronics(III)", 
            "Microprocessor"
            
            ],
        "mail": "411074050@mail.nknu.edu.tw",
        "activation_code": "411074050",
        "status": "standard",
        "level": 0,
        "identity": "none"
    },
    {
        "user_id": "王昱潔",
        "stu_name": "王昱潔",
        "stu_gender": "female",
        "stu_id": "411074051",
        "stu_subject": [
            
            "Microelectronics Circuits Experiment and Design(II)", 
            "Microprocessor"
            
            ],
        "mail": "411074051@mail.nknu.edu.tw",
        "activation_code": "411074051",
        "status": "standard",
        "level": 0,
        "identity": "none"
    },
    {
        "user_id": "林鈺淳",
        "stu_name": "林鈺淳",
        "stu_gender": "female",
        "stu_id": "411074053",
        "stu_subject": [
            
            "Introduction to Microwave", 
            "Microelectronics Circuits Experiment and Design(II)", 
            "Physics of Semiconductor Devices", 
            "Introduction to Optoelectronic"
            
            ],
        "mail": "411074053@mail.nknu.edu.tw",
        "activation_code": "411074053",
        "status": "standard",
        "level": 0,
        "identity": "none"
    }
   
]
mycol.insert_many(students_data)
