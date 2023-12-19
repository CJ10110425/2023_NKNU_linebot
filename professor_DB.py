import pymongo
import dotenv
import os
from pathlib import Path
import json
from pymongo.collection import Collection
from pymongo.database import Database
from pymongo.errors import BulkWriteError, ConnectionFailure
import pprint
from timeit import default_timer as timer

validation_path = Path("data_validation.json")

dotenv.load_dotenv()  #Preparing your URL

with open(validation_path, "r") as file:
    validation_data = json.load(file)

#Check the connection
try:
    client = pymongo.MongoClient(os.getenv("MONGODB_URL"))
    nknu_linebot_db = client["2023_nknu_linebot"]
except ConnectionFailure as e:
    print(f"Connection failure: {e}")


db_name = "professors_db"

#Create a professor's database 
collection_list = nknu_linebot_db.list_collection_names()
    
if db_name not in collection_list:
    professors_db = nknu_linebot_db.create_collection(db_name, validator=validation_data["professors_db"])
else:
    professors_db = nknu_linebot_db.get_collection(db_name)

professors_db.create_index(["user_id", "alpha_upper_score", "alpha_lower_score", "integer_score"])
  
def create_db(db_name: str) -> Database:
    '''create a database and returning a database'''
    collection_list = nknu_linebot_db.list_collection_names()
        
    if db_name not in collection_list:
        database  = nknu_linebot_db.create_collection(db_name, validator=validation_data["professors_db"])
    else:
        database = nknu_linebot_db.get_collection(db_name)  
    
    return database

#Return a validation schema configuration
def find_data_config(col_name: Collection=professors_db) -> list:

    valid_config = validation_data[col_name.name]["$jsonSchema"]["properties"]
    valid_config_list = list(valid_config.keys())
    
    return valid_config_list


#Store data into database
def store_profeesor_info(data: dict,
                         col_name: Collection=professors_db) -> None:
    
    professor_info = col_name.find_one({"user_id": data["user_id"]})
    
    score = score_mechanism(user_id=data["user_id"])
    
    data = {**data, **score}
    
    if professor_info is None:
        try:
            col_name.insert_one(data) 
        except BulkWriteError as e:
            print(f"ValidationError: {e.details['writeEorrors'][0]['errmsg']}")
    

def delete_data(user_id: str,
                col_name: Collection=professors_db) -> int:
    """
    可以將指定的user_id刪除
    當回傳值為零時，代表刪除失敗，可能並未有此資料
    當回傳直不為零時，表示刪除幾組資料
    """
    
    delete_result = col_name.delete_one({"user_id": user_id})
    
    return delete_result.deleted_count()
                                                                       
                                                                       
def update_data(user_id: str,
                update_data: dict,
                col_name: Collection=professors_db) -> dict:
    
    """
    
    更新集合中的資料
    當有不符合驗證集合的更新資料 raise ValueError
    
    """
    wrongdoc = []
    
    data_config = find_data_config(col_name)
    update_config = list(update_data.keys())
    
    for data in update_config:
        if data not in data_config:
            del update_data[data]
            wrongdoc.append(data)
        
    result = col_name.update_one(filter={"user_id": user_id}, update={"$set": update_data})
    results = {"modified": result.modified_count, "wrongdoc": wrongdoc}
    
    return results
    

def find_professor_info(user_id: str,
                        select_info: list[str] or str,
                        col_name: Collection=professors_db) -> list[dict] or list:
    
    """col_name是放pymongo.collection的集合，預設值為professor_db"""
    
    results = col_name.find_one({"user_id": user_id})
    
    classes = {}
    clas = str
    
    if isinstance(select_info, list):
        for info in select_info:
            classes[info] = results[info]
        return classes
    
    elif isinstance(select_info, str):
        clas = results[select_info]
        return clas


def find_professor_different_info(user_id: str,
                                  select_info: list[str] or str,
                                  col_name: Collection=professors_db) -> list[dict] or list:
    
    """col_name是放pymongo.collection的集合，預設值為professor_db"""
    
    projection = {"_id": False}
    
    for mask in select_info:
        projection[mask] = True
    
    results = col_name.find(filter={"user_id":user_id}, projection=projection)
    
    results = results["pro_gender"]
    
    return results


def get_userid(col_name: Collection=professors_db):
    
    data = col_name.find(filter={}, projection={"user_id": True, "_id": False})
    
    return data


def score_mechanism(user_id: str) -> dict[str: int]:
    
    alpha_upper_score = 0
    alpha_lower_score = 0
    integer_score = 0

    for alphabet in user_id:
        if alphabet.isalpha():
            if alphabet.isupper():
                alpha_upper_score += ord(alphabet)
            else:
                alpha_lower_score += ord(alphabet)
        else:
            integer_score += ord(alphabet)
    
    result = {"alpha_upper_score": alpha_upper_score, "alpha_lower_score": alpha_lower_score, "integer_score": integer_score}
    
    return result

def finding_test(user_id: dict,
                 col_name: Collection=professors_db):
    
    result = score_mechanism(user_id=user_id["user_id"])
    index = {**user_id, **result}
    
    document = col_name.find_one(filter=index)
    
    return document
     
if __name__ == "__main__":
    
    printer = pprint.PrettyPrinter()

    printer.pprint(finding_test(user_id={"user_id": "2"}))
    
    # update_data1 = {"pro_gender": "male", "status": "none", "level": 1}
    # result = update_data(user_id="2", update_data={"pro_gend": "male"})
    # print(result)
    
    # data1 = find_professor_different_info(user_id="1", select_info=["teach_subject","pro_gender"])
    # print(data1)
    
    # data2 = find_professor_info(user_id="1", select_info=["teach_subject", "pro_gender"])
    # print(data2)
    
    # start_time = timer()
    
    # data = get_userid()
    
    # printer.pprint(list(data))
    
    # end_time = timer()
    
    # print(f"{end_time - start_time:.3f}")