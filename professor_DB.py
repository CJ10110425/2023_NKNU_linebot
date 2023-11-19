import pymongo
import dotenv
import os
from pathlib import Path
import json
from datetime import datetime as dt
from pymongo.errors import BulkWriteError

dotenv.load_dotenv()  # Preparing your MONGODB_URL


client = pymongo.MongoClient(os.getenv("MONGODB_URL"))
validation_path = Path("data_validation.json")


with open(validation_path, "r") as file:

    json_and_doc = json.load(file)

validation_rules = json_and_doc["validation_rules"]
doc = json_and_doc["document"]["insert_test"]


def insert_data(data: dict) -> None:
    """
    This function create collections and inserting data.

    Args:
        data: It should contains professor_name, subject and assignment.

    Example:
        data = {"professor_name": "Jason Zheng",
                "subject_name": "English",
                "assignment": "Homework: A to B"}
    """

    professor_db = client.get_database(data["professor"])
    existing_collection = professor_db.list_collection_names()

    if data["subject"] not in existing_collection:
        collection = professor_db.create_collection(
            data["subject"], validation=validation_rules["insert_validation"])

    data["date"] = dt.now()

    try:
        collection.insert_one(data)
    except BulkWriteError as e:
        print(f"Validadtion: {e.details['writeErrors'][0]['errmsg']}")


def delete_data(professor: str,
                subject: str,
                delete_target: dict) -> None:

    professor_db = client.get_database(professor)
    collection = professor_db.get_collection(subject)

    try:
        collection.delete_one(delete_target)
    except ValueError:
        print("This data is not in the collection")


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


if __name__ == '__main__':

    print("[INFO] Test is successful")
    insert_data(doc)
