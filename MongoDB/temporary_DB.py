import pymongo
import dotenv
import os

dotenv.load_dotenv()
## 下面連結得自行連結 ##
myclient = pymongo.MongoClient(
    os.getenv("MONGODB_URL"), tls=True, tlsAllowInvalidCertificates=True)
mydb = myclient["2023_nknu_linebot"]
mycol = mydb["temporary_DB"]


def find_profile(user_id):
    '''
    find profile
    '''
    return mycol.find_one({"user_id": user_id})
    # return mycol.find_one({"user_id": user_id}, {"_id": 0})
    # return mycol.find_one({"user_id": user_id}, {"_id": 0, "user_id": 0})
    # return mycol.find_one({"user_id": user_id}, {"_id": 0, "user_id": 0, "identity": 0})
    # return mycol.find_one({"user_id": user_id}, {"_id": 0, "user_id": 0, "identity": 0, "name": 0})
    # return mycol.find_one({"user_id": user_id}, {"_id": 0, "user_id": 0, "identity": 0, "name": 0, "mail": 0})
def find_identity(user_id):
    '''
    find identity
    '''
    return mycol.find_one({"user_id": user_id}, {"identity": 1})
def insert_profile(user_id,identity, name, mail,activation_code):
    '''
    initial profile
    '''
    mycol.insert_one({"user_id": user_id,"identity":identity,
                     "name": name,"mail": mail, "activation_code": activation_code})

def update_name(user_id, name):
    '''
    update name
    '''
    mycol.update_one({"user_id": user_id}, {"$set": {"name": name}})

def update_mail(user_id, mail):
    '''
    update mail
    '''
    mycol.update_one({"user_id": user_id}, {"$set": {"mail": mail}})

def update_activation_code(user_id, activation_code):
    '''
    update activation_code
    '''
    mycol.update_one({"user_id": user_id}, {"$set": {"activation_code": activation_code}})

def update_identity(user_id, identity):
    '''
    update identity
    '''
    mycol.update_one({"user_id": user_id}, {"$set": {"identity": identity}})

def delete_profile(user_id):
    '''
    delete profile
    '''
    mycol.delete_one({"user_id": user_id})
    # mycol.delete_one({"user_id": user_id}, {"_id": 0})
    # mycol.delete_one({"user_id": user_id}, {"_id": 0, "user_id": 0})
    # mycol.delete_one({"user_id": user_id}, {"_id": 0, "user_id": 0, "identity": 0})
    # mycol.delete_one({"user_id": user_id}, {"_id": 0, "user_id": 0, "identity": 0, "name": 0})
    # mycol.delete_one({"user_id": user_id}, {"_id": 0, "user_id": 0, "identity": 0, "name": 0, "mail": 0}) 

if __name__ == "__main__":
    a = find_identity("Ua228ca9743237fb1fb497b4b3d0247c9")
    print(a["identity"])