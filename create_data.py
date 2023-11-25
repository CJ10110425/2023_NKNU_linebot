import professor_DB as pro
import json
from pathlib import Path

professor_data = Path("professor_data.json")

with open(professor_data, "r", encoding="utf-8") as file:
    pro_data = json.load(file)

pro_db = pro.create_database("professors_db")

for data in pro_data["pro_document"]:
    print("[INFO] Insert successful")
    pro.store_info(col_name=pro_db,
                   data=data)
    

