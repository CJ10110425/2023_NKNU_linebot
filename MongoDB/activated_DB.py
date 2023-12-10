import pymongo
import dotenv
import os
import logging as log
dotenv.load_dotenv()
## 下面連結得自行連結 ##
myclient = pymongo.MongoClient(
    os.getenv("MONGODB_URL"), tls=True, tlsAllowInvalidCertificates=True)
mydb = myclient["2023_nknu_linebot"]
mycol = mydb["activated_accounts"]


def insert_profile(user_id, status, level, identity):
    '''
    initial profile
    '''
    mycol.insert_one({"user_id": user_id,
                     "status": status, "level": level, "identity": identity})


def check_profile(user_id):
    '''
    check profile
    '''
    profile = mycol.find_one({"user_id": user_id})
    if profile is None:
        insert_profile(user_id, "standard", 0, "visitor")
        return {"status": "standard", "level": 0, "identity": "visitor"}
    else:
        return profile


def update_level(user_id, level):
    result = mycol.update_one({"user_id": user_id}, {"$set": {"level": level}})
    log.info(result)


def delete_profile(user_id):
    mycol.delete_one({"user_id": user_id})
    # mycol.delete_one({"user_id": user_id}, {"_id": 0})
    # mycol.delete_one({"user_id": user_id}, {"_id": 0, "user_id": 0})
    # mycol.delete_one({"user_id": user_id}, {"_id": 0, "user_id": 0, "identity": 0})
    # mycol.delete_one({"user_id": user_id}, {"_id": 0, "user_id": 0, "identity": 0, "name": 0})
    # mycol.delete_one({"user_id": user_id}, {"_id": 0, "user_id": 0, "identity": 0, "name": 0, "mail": 0})


def update_all_to_none(user_id):
    mycol.update_many({"user_id": user_id}, {
                      "$set": {"status": "standard", "level": 0, "identity": "visitor"}})
    # mycol.update_many({"user_id": user_id}, {"$set": {"status": "none", "level": 0, "identity": "visitor", "name": "none", "mail": "none", "activation_code": "none"}})
    # mycol.update_many({"user_id": user_id}, {"$set": {"status": "none", "level": 0, "identity": "visitor", "name": "none", "mail": "none"}})
    # mycol.update_many({"user_id": user_id}, {"$set": {"status": "none", "level": 0, "identity": "visitor", "name": "none"}})
    # mycol.update_many({"user_id": user_id}, {"$set": {"status": "none", "level": 0, "identity": "visitor"}})


def update_status(user_id, status):
    mycol.update_one({"user_id": user_id}, {"$set": {"status": status}})
    # mycol.update_one({"user_id": user_id}, {"$set": {"status": status, "name": "none", "mail": "none", "activation_code": "none"}})
    # mycol.update_one({"user_id": user_id}, {"$set": {"status": status, "name": "none", "mail": "none"}})
    # mycol.update_one({"user_id": user_id}, {"$set": {"status": status, "name": "none"}})
    # mycol.update_one({"user_id": user_id}, {"$set": {"status": status}})

def update_identity(user_id, identity):
    mycol.update_one({"user_id": user_id}, {"$set": {"identity": identity}})
    # mycol.update_one({"user_id": user_id}, {"$set": {"identity": identity, "name": "none", "mail": "none", "activation_code": "none"}})
    # mycol.update_one({"user_id": user_id}, {"$set": {"identity": identity, "name": "none", "mail": "none"}})
    # mycol.update_one({"user_id": user_id}, {"$set": {"identity": identity, "name": "none"}})
    # mycol.update_one({"user_id": user_id}, {"$set": {"identity": identity}})


if __name__ == "__main__":
    insert_profile("test", "test", "test", "test", "test")
