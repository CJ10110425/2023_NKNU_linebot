import pymongo
import dotenv
import os
from pathlib import Path
import json
from datetime import datetime as dt
from pymongo.errors import BulkWriteError

dotenv.load_dotenv()  # Preparing your MONGODB_URL

validation_path = Path("data_validation.json")

with open(validation_path, "r") as file:

    json_and_doc = json.load(file)

validation_rules = json_and_doc["validation_rules"]
test_doc = json_and_doc["document"]["insert_test"]

client = pymongo.MongoClient(os.getenv("MONGODB_URL"))
nknu_linebot_db = client["NKNU_DataBase"]


def create_professor_database(db_name: str) -> pymongo.CursorType:
    
    collection_list = nknu_linebot_db.list_collection_names()
    
    if db_name not in collection_list:
        professor_db = nknu_linebot_db.create_collection(db_name, validator=validation_rules)
    else:
        professor_db = nknu_linebot_db.find(db_name)

    return professor_db


def create_professor_info(db_name: pymongo.CursorType,
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
    professor_info = db_name.find({"name": data["name"]})
    
    if professor_info is None:
        try:
            db_name.insert_one(data) 
            print("[INFO] Insert successful")
        except BulkWriteError as e:
            print(f"ValidationError: {e.details['writeEorrors'][0]['errmsg']}")
    

def delete_data(db_name: pymongo.CursorType,
                delete_name: str) -> None:
    
    db_name.delete_one({"name": delete_name})
    
    
def update_data(professor: str,
                update_target: [str, dict]) -> None:

    subject = update_target[0]
    professor_db = client.get_database(professor)
    collection = professor_db.get_collection(subject)

    try:
        collection.delete_one(update_target[1])
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
    
    test_DB = create_professor_database("professor_database")
    print(test_DB)


if __name__ == '__main__':

    print("[INFO] Test is successful")
