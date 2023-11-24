import pymongo
import dotenv
import os
import json

dotenv.load_dotenv()


myclient = pymongo.MongoClient(
    os.getenv("MONGODB_URL"), tls=True, tlsAllowInvalidCertificates=True)
mydb = myclient["2023_nknu_linebot"]
mycol = mydb["student_profile"]

# 打開 JSON 檔案並讀取內容
with open('database.json', 'r', encoding='utf-8') as json_file:
    students_data = json.load(json_file)

if __name__ == "__main__":
    # mycol.insert_many(students_data)
    pass
