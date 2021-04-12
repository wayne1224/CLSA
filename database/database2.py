import pymongo
import datetime
import time
import calendar
from werkzeug.local import LocalProxy
from bson.objectid import ObjectId

# connect database
def get_db():
    client = pymongo.MongoClient("mongodb://m001-student:m001-mongodb-basics@sandbox-shard-00-00.b61rz.mongodb.net:27017,sandbox-shard-00-01.b61rz.mongodb.net:27017,sandbox-shard-00-02.b61rz.mongodb.net:27017/test?replicaSet=atlas-r9j9pm-shard-0&ssl=true&authSource=admin")
    db = client["Test"] # choose database
    # db = LocalProxy(get_db) # Use LocalProxy to read the global db instance with just 'db'
    CLSA = db["CLSA"] # choose collection

    return CLSA

def upsertBasic(info): # info = [ObjectId , caseID , version , doctor , patientData , location , form , date , participants , recordType , help , situation , others]
    db = get_db()

    if info[0] == "":  # insert new data
        query = dict()
        query["caseID"] = info[1]
        
        version = db.count_documents(query) + 1

        data = {
            "caseID" : info[1],
            "version" : version,
            "doctor" : info[3],
            "patientData" : info[4],
            "location" : info[5],
            "form" : info[6],
            "date" : info[7],
            "participants" : info[8],
            "recordType" : info[9],
            "help" : info[10],
            "situation" : info[11],
            "others" : info[12],
            "content" : "no content",
            "analysis" : "no analysis"
        }

        db.insert_one(data)
    else:  # update data
        query = dict()
        query["_id"] = info[0]

        data = {
            "caseID" : info[1],
            "version" : info[2],
            "doctor" : info[3],
            "patientData" : info[4],
            "location" : info[5],
            "form" : info[6],
            "date" : info[7],
            "participants" : info[8],
            "recordType" : info[9],
            "help" : info[10],
            "situation" : info[11],
            "others" : info[12],
        }

        data = {"$set" : data} 
        db.update(query , data)

def readByCaseID(ID): 
    db = get_db()
    query = dict()
    query["caseID"] = ID

    # 檢查個案編號是否存在 , 不存在 => error
    if db.count_documents(query) == 0:
        print("此個案編號不存在")
        return

    data = db.find(query)

    for i in data:
        print(i)


date = datetime.datetime.strptime("2018-01-31", "%Y-%m-%d")
objID = ObjectId("60729d1fc791aec07244a7d9")

# # insert new data
# info1 = ["" , "001" , 1 , "doctor" , {"name" : "123"} , "location" , "form" , date , ["Dad" , "Mom"] , "recordType" , "help" , "situation" , "others"]
# upsertBasic(info1)

# # update data
# info2 = [objID , "002" , "" , "doctor123" , {"name" : "123"} , "location" , "form" , date , ["Dad" , "Mom"] , "recordType" , "help" , "situation" , "others"]
# upsertBasic(info2)

readByCaseID("001")





            




