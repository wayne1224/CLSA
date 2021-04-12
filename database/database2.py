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
        
        # version = db.count_documents(query) + 1

        data = {
            "caseID" : info[1],
            # "version" : version,
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

        db.insert_one(data)
    else:  # update data
        query = dict()
        query["_id"] = info[0]

        data = {
            "caseID" : info[1],
            # "version" : info[2],
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

def upsertContent(info): # info = [ObjectId , caseID , content] , content是一個list裡面的每個物件為dict
    db = get_db()

    if info[0] == "":  # insert new data
        query = dict()
        query["caseID"] = info[1]
        
        data = {
            "caseID" : info[1],
            "content" : info[2]
        }

        db.insert_one(data)
    else:  # update data
        query = dict()
        query["_id"] = info[0]

        data = {
            "caseID" : info[1],
            "content" : info[2]
        }

        data = {"$set" : data} 
        db.update_one(query , data)

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
objID = ObjectId("607455182078fa7d5e9d01f3")

a1 = {"ID" : "a1" , "rule" : "adult" , "utterance" : "1234" , "scenario" : "123"}
a2 = {"ID" : "1" , "rule" : "child" , "utterance" : "123" , "scenario" : "123"}
a3 = {"ID" : "" , "rule" : "" , "utterance" : "" , "scenario" : "123"}

content = [a1 , a2 , a3]

# insert new basic
# info1 = ["" , "001" , 1 , "doctor" , {"name" : "123"} , "location" , "form" , date , ["Dad" , "Mom"] , "recordType" , "help" , "situation" , "others"]
# upsertBasic(info1)

# update basic
# info2 = [objID , "001" , "" , "doctor123" , {"name" : "123"} , "location" , "form" , date , ["Dad" , "Mom"] , "recordType" , "help" , "situation" , "others"]
# upsertBasic(info2)

# insert new content
# info3 = ["", "001" , content]
# upsertContent(info3)

# update content
# info4 = [objID , "001" , content]
# upsertContent(info4)

# readByCaseID("001")





            




