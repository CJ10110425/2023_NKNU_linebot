import students_functions
import pymongo
import dotenv
import os
import json

dotenv.load_dotenv()

## 下面連結得自行連結 ##
myclient = pymongo.MongoClient(os.getenv("MONGODB_URL"))
mydb = myclient["2023_nknu_linebot"]
mycol = mydb["student_profile"]

# 打開 JSON 檔案並讀取內容
with open('database.json', 'r', encoding='utf-8') as json_file:
    students_data = json.load(json_file)


mycol.insert_many(students_data)
