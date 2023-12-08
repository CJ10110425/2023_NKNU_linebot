import pymongo
import dotenv
import os
from pymongo.collection import Collection
from pymongo.errors import BulkWriteError, ConnectionFailure
import pprint
import professor_DB as pro_fn
from datetime import datetime as dt

dotenv.load_dotenv()

printer = pprint.PrettyPrinter()

try:
    client = pymongo.MongoClient(os.getenv("MONGODB_URL"))
    nknu_linebot_db = client["2023_nknu_linebot"]
except ConnectionFailure as e:
    print(f"Connection failure: {e}")
    
pro_cache = nknu_linebot_db["pro_cache"]

def find_pro_list():
    
    pro_list = pro_cache.find_one({"storetype": "pro_list"})
    
    return pro_list

def store_cache(title: str, **kwargs):
    
    data = {
        "title": title,
        "content": kwargs,
        "date": dt.now()
    }
    pro_cache.insert_one(data)
