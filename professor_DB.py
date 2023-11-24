import pymongo
import dotenv
import os
from pathlib import Path
import json
from pymongo.collection import Collection
from pymongo.errors import BulkWriteError, ConnectionFailure

dotenv.load_dotenv()  # Preparing your MONGODB_URL

validation_path = Path("data_validation.json")
test_doc = Path("test_data.json")

with open(validation_path, "r") as file:
    validation_data = json.load(file)

with open(test_doc, "r") as file:
    test_doc = json.load(file)

validation_rules = validation_data
test_doc = test_doc["test_document"]


try:
    client = pymongo.MongoClient(os.getenv("MONGODB_URL"))
    nknu_linebot_db = client["2023_nknu_linebot"]
except ConnectionFailure as e:
    print(f"Connection failure: {e}")


def find_data_config(db_name: Collection) -> list:
    
    valid_config = validation_rules[str(db_name.name)]["$jsonSchema"]["properties"]
    valid_config_list = list(valid_config.keys())
    
    return valid_config_list


def create_database(db_name: str) -> Collection:
    
    """
    This function create a database with a schema valdation, and returning 
    a collection.
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
    This function create collections and inserting data.

    Args:
        data: It should contains name, gender, subject_taught.
        
    Example:
        data = {"Name": "Jason Zheng",
                "Gender": "male",
                "Subject_Taught": "English"}
    """
    
    professor_info = col_name.find_one({"user_id": data["user_id"]})
    
    if professor_info is None:
        try:
            col_name.insert_one(data) 
            print("[INFO] Insert successful")
        except BulkWriteError as e:
            print(f"ValidationError: {e.details['writeEorrors'][0]['errmsg']}")
    

def delete_data(db_name: Collection,
                user_id: str) -> None:
    
    db_name.delete_one({"user_id": user_id})
                                                                       
    
    
def update_data(db_name: Collection,
                user_id: str,
                update_data: dict) -> None:
    
    data_config = find_data_config(db_name)
    update_config = list(update_data.keys())
    
    for data in update_config:
        if data not in data_config:
            raise ValueError(f"The update data does not match validation schema")
    
    amount = len(update_data)
    
    if amount == 1:
        db_name.update_one({"user_id": user_id}, {"$set": update_data})
    try:
        db_name.delete_one(update_data[1])
    except ValueError:
        print(f"This data is not in the collection")


def find_data(professor: str,
              find_target: dict) -> None:

    subject = find_target["subject"]
    target_date = find_target["date"]

    professor_db = client.get_database(professor)
    collection = professor_db.get_collection(subject)

    try:
        collection.find_one({"date": target_date})
    except ValueError:
        print(f"This data is not in the collection")
    

def add_data(db_name: pymongo.CursorType,
             add_data: dict) -> pymongo.CursorType: 
    
    return db_name.insert_one(add_data)


if __name__ == '__main__':

    print("[INFO] Test is successful")
    pro_db = create_database(db_name="professors_db")

    lista = find_data_config(pro_db)
    print(lista)
    
    # if pro_db is not None:
    #     print(f"[INFO] create successfully {pro_db.type}")
        
    # for simple in test_doc:
    #     create_professor_info(col_name=pro_db,
    #                           data=simple)
    
    # result = add_data(db_name=pro_db,
    #          add_data=test_doc[0])
    
    # print(result)