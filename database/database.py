import pymongo
import datetime
import time
import calendar
from werkzeug.local import LocalProxy

# connect database
def get_db():
    client = pymongo.MongoClient("mongodb://m001-student:m001-mongodb-basics@sandbox-shard-00-00.b61rz.mongodb.net:27017,sandbox-shard-00-01.b61rz.mongodb.net:27017,sandbox-shard-00-02.b61rz.mongodb.net:27017/test?replicaSet=atlas-r9j9pm-shard-0&ssl=true&authSource=admin")
    db = client["Test"] # choose database
    # db = LocalProxy(get_db) # Use LocalProxy to read the global db instance with just 'db'
    CLSA = db["CLSA"] # choose collection

    return CLSA

# CRUD

# 這是一個新的檔案
def createBasic(info): # info = [ID , doctor , patientData , location , form , date , participants , recordType , help , situation , others]
    db = get_db()
    query = dict()
    query["caseID"] = info[0]
    
    version = db.count_documents(query) + 1

    data = {
        "caseID" : info[0],
        "version" : version,
        "doctor" : info[1],
        "patientData" : info[2],
        "location" : info[3],
        "form" : info[4],
        "date" : info[5],
        "participants" : info[6],
        "recordType" : info[7],
        "help" : info[8],
        "situation" : info[9],
        "others" : info[10],
        "content" : "no content",
        "analysis" : "no analysis"
    }

    db.insert_one(data)

# 依據caseID , date當作判斷要修改哪個
def updateBasic(info): # info = [ID , doctor , patientData , location , form , date , participants , recordType , help , situation , others]
    db = get_db()
    query = dict()
    query["caseID"] = info[0] # caseID
    query["date"] = info[5] # date

    # 檢查是否存在 , 不存在 => error
    if db.count_documents(query) == 0:
        print("此檔案不存在")
        return

    origin = db.find(query)

    data = {
        "caseID" : info[0],
        "version" : origin[0]["version"],
        "doctor" : info[1],
        "patientData" : info[2],
        "location" : info[3],
        "form" : info[4],
        "date" : info[5],
        "participants" : info[6],
        "recordType" : info[7],
        "help" : info[8],
        "situation" : info[9],
        "others" : info[10],
        "content" : "no content",
        "analysis" : "no analysis"
    }

    data = {"$set" : data} 
    db.update(query , data)

# 依據caseID , date當作判斷要修改哪個
def updateContent(info): # info = [ID , date , content]
    db = get_db()
    query = dict()
    query["caseID"] = info[0] # caseID
    query["date"] = info[1] # date

    # 檢查是否存在 , 不存在 => error
    if db.count_documents(query) == 0:
        print("此檔案不存在")
        return

    data = {"$set" : {"content" : info[2]}}
    db.update(query, data)

# 找出所有相同caseID的檔案
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

# 依據caseID , date當作判斷要刪除哪個
def delete(info):
    db = get_db()
    query = dict()
    query["caseID"] = info[0] # caseID
    query["date"] = info[1] # date

    # 檢查是否存在 , 不存在 => error
    if db.count_documents(query) == 0:
        print("此檔案不存在")
        return
    
    db.delete_one(query)

date = datetime.datetime.strptime("2018-01-31", "%Y-%m-%d")

a1 = {"num" : "1" , "type" : "child" , "script" : "GGININ" , "scenario" : "123"}
a2 = {"num" : "A1" , "type" : "adult" , "script" : "GGININ" , "scenario" : "123"}
a3 = {"num" : "" , "type" : "scenario" , "script" : "" , "scenario" : "123"}

content = [a1 , a2 , a3]

# info1 = ["001" , "doctor" , {"name" : "123"} , "location" , "form" , date , ["Dad" , "Mom"] , "recordType" , "help" , "situation" , "others"]
# createBasic(info1)

# info2 = ["001" , "doctor123456" , {"name" : "123"} , "location" , "form" , date , ["Dad" , "Mom"] , "recordType" , "help" , "situation" , "others"]
# updateBasic(info2)

# info3 = ["001" , date , content]
# updateContent(info3)

# info4 = ["001" , date]
# delete(info4)

readByCaseID("001")
