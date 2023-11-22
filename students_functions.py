import pymongo
import dotenv
import os
dotenv.load_dotenv()

## 下面連結得自行連結 ##
myclient = pymongo.MongoClient(
    os.getenv("MONGODB_URL"), tls=True, tlsAllowInvalidCertificates=True)
mydb = myclient["2023_nknu_linebot"]
mycol = mydb["student_profile"]


def insert_userprofile(user_id, stu_name, stu_gender, stu_id, stu_subject, mail, activation_code, status, level, identity):
    '''
    學生的基本資料
    '''
    mycol.insert_one({"user_id": user_id, "stu_name": stu_name, "stu_gender": stu_gender, "stu_id": stu_id, "stu_subject": stu_subject,
                      "mail": mail, "activation_code": activation_code, "status": status, "level": level, "identity": identity})


def find_information_by_userid(user_id, information=["stu_name", "stu_gender", "stu_gender", "stu_id", "stu_subject", "mail", "activation_code", "status", "level", "identity"]) -> (int, str):
    '''
    level屬性為int,其餘為string
    鎖定想查詢的學生id 
    '''

    query = {"user_id": {"$in": [user_id]}}
    '''
    找尋鎖定學生的資料
    '''
    results = mycol.find(query)
    classes = []
    for result in results:
        print(result)
        classes.append(result[information])
    return classes

def find_userid_by_course(target_student_class):
    '''
    從學生的課程找尋學生的ID
    '''

    IDs = []
    '''
    鎖定想查詢課程
    '''

    query = {"stu_subject": {"$in": [target_student_class]}}
    '''
    找尋符合相同資料的人
    '''
    results = mycol.find(query)
    
    '''
    接續將相同課程的學生的 "Student_name" 這組資料由 append接續儲存至results
    '''
    for result in results:
        print (results)
        IDs.append(result["user_id"])
    return IDs



def update_attributes(user_id, new_attribute, attributes=["stu_name", "stu_gender", "stu_gender", "stu_id", "stu_subject", "mail", "activation_code", "status", "level", "identity"]) -> None:
    '''
    更新level需要轉成int
    '''

    mycol.update_one({"user_id": user_id}, {
                     "$set": {attributes: new_attribute}})


if __name__ == "__main__":
    print()
