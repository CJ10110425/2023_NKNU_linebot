import pymongo
import dotenv
import os
from pathlib import Path
import json
from pymongo.collection import Collection
from pymongo.errors import BulkWriteError, ConnectionFailure

dotenv.load_dotenv()  # 準備自己資料庫的URL


validation_path = Path("data_validation.json")


with open(validation_path, "r") as file:
    validation_data = json.load(file)

validation_rules = validation_data["professors_db"]


try:
    client = pymongo.MongoClient(os.getenv("CJJS"))
    nknu_linebot_db = client["2023_nknu_linebot"]
except ConnectionFailure as e:
    print(f"Connection failure: {e}")


def find_data_config(db_name: Collection) -> list:
    """
    
    回傳資料驗證格式
    
    """
    valid_config = validation_rules[str(db_name.name)]["$jsonSchema"]["properties"]
    valid_config_list = list(valid_config.keys())
    
    return valid_config_list


def create_database(db_name: str) -> Collection:
    
    """
    
    建立教授的資料庫
    
    """
    
    collection_list = nknu_linebot_db.list_collection_names()
    
    if db_name not in collection_list:
        professor_db = nknu_linebot_db.create_collection(db_name, validator=validation_rules)
    else:
        professor_db = nknu_linebot_db.get_collection(db_name)

    return professor_db


def store_info(col_name: Collection,
               data: dict) -> None:
    
    """
    
    將資料存進所指定的資料集合
    
    """
    
    professor_info = col_name.find_one({"user_id": data["user_id"]})
    
    if professor_info is None:
        try:
            col_name.insert_one(data) 
        except BulkWriteError as e:
            print(f"ValidationError: {e.details['writeEorrors'][0]['errmsg']}")
    

def delete_data(col_name: Collection,
                user_id: str) -> int:
    """
    
    可以將指定的user_id刪除
    當回傳值為零時，代表刪除失敗，可能並未有此資料
    當回傳直不為零時，表示刪除幾組資料
    
    """
    
    delete_result = col_name.delete_one({"user_id": user_id})
    
    return delete_result.deleted_count()
                                                                       
                                                                       
def update_data(col_name: Collection,
                user_id: str,
                update_data: dict) -> dict:
    
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


def find_data(col_name: Collection,
              user_id: str) -> dict or None:
    
    """
    
    找尋集合中所符合的資料
    
    """
    
    result = col_name.find_one({"user_id": user_id})
    
    return result
