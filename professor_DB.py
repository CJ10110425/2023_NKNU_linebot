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


dotenv.load_dotenv()  # Preparing your URL


validation_path = Path("data_validation.json")

printer = pprint.PrettyPrinter()

with open(validation_path, "r") as file:
    validation_data = json.load(file)

validation_rules = validation_data["professors_db"]

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
    professor_db = nknu_linebot_db.create_collection(db_name, validator=validation_rules)
else:
    professor_db = nknu_linebot_db.get_collection(db_name)
  
  
def create_db(db_name: str) -> Database:
    '''create a database and returning a database'''
    collection_list = nknu_linebot_db.list_collection_names()
        
    if db_name not in collection_list:
        database  = nknu_linebot_db.create_collection(db_name, validator=validation_rules)
    else:
        database = nknu_linebot_db.get_collection(db_name)  
    
    return database

#Return a validation schema configuration
def find_data_config(db_name: Collection=professor_db) -> list:

    valid_config = validation_rules[str(db_name.name)]["$jsonSchema"]["properties"]
    valid_config_list = list(valid_config.keys())
    
    return valid_config_list


#Store data into database
def store_profeesor_info(data: dict,
               col_name: Collection=professor_db) -> None:
    
    professor_info = col_name.find_one({"user_id": data["user_id"]})
    
    if professor_info is None:
        try:
            col_name.insert_one(data) 
        except BulkWriteError as e:
            print(f"ValidationError: {e.details['writeEorrors'][0]['errmsg']}")
    

def delete_data(user_id: str,
                col_name: Collection=professor_db) -> int:
    """
    可以將指定的user_id刪除
    當回傳值為零時，代表刪除失敗，可能並未有此資料
    當回傳直不為零時，表示刪除幾組資料
    """
    
    delete_result = col_name.delete_one({"user_id": user_id})
    
    return delete_result.deleted_count()
                                                                       
                                                                       
def update_data(user_id: str,
                update_data: dict,
                col_name: Collection=professor_db) -> dict:
    
    """
    
    更新集合中的資料
    當有不符合驗證集合的更新資料 raise ValueError
    
    """
    
    data_config = find_data_config(col_name)
    update_config = list(update_data.keys())
    
    for data in update_config:
        if data not in data_config:
            raise ValueError(f"The update data does not match validation schema")
    
    result = col_name.update_one({"user_id": user_id}, {"$set": update_data})
    returndata = {"modified_info": result.modified_count, "changed_info": data_config}
    
    return returndata


def find_professor_info(user_id: str,
                        select_info: list[str] or str,
                        col_name: Collection=professor_db) -> list[dict] or list:
    
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
            

def get_userid(col_name: Collection=professor_db):
    
    data = col_name.find(filter={}, projection={"user_id":1, "_id": False})
    
    return data
    
     
if __name__ == "__main__":

    data = find_professor_info(user_id="1", select_info=["teach_subject", "pro_gender"])
    print(data)
    # start_time = timer()
    
    # data = get_userid()
    
    # printer.pprint(list(data))
    
    # end_time = timer()
    
    # print(f"{end_time - start_time:.3f}")