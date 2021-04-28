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

# 查詢頁 api
def findDoc(SLP , caseID , name): # argument = SLP , caseID , name, if find return pymongo object , else return False
    db = get_db()
    query = dict()

    if SLP:
        query["include.SLP"] = SLP
    if caseID:
        query["childData.caseID"] = caseID
    if name:
        query["childData.name"] = name

    if db.count_documents(query) == 0:
        print("can not find this document")
        return False

    return db.find(query)
    
# 收錄表 api
def findChildData(caseID): # argument = caseID , if find return childData (type = dict) , else return False
    db = get_db()
    query = dict()
    query["childData.caseID"] = caseID

    if db.count_documents(query) == 0:
        print("can not find this caseID")
        return False

    return db.find_one(query)["childData"]

def upsertChildAndInclude(childData , include): # argument = childData , include
    db = get_db()
    query = dict()
    query["childData.caseID"] = childData["caseID"]
    query["include.date"] = include["date"]  


    # 更新收錄表
    if db.count_documents(query) != 0: 
        a = db.update_one(query , {"$set" : {"childData" : childData , "include" : include}})
        print("document updates successfully")

    # 插入新的收錄表  
    else:
        data = {
            "childData" : childData,
            "include" : include,
            "transcribe" : {"transcriber" : None, 
                            "content" : None,
                            "anaylsis" : None,
                            "totalUtterance" : None,
                            "validUtterance" : None
            } 
        }

        db.insert_one(data)
        print("document inserts successfully")
    
    # 更新舊的childData
    query = dict()
    query["childData.caseID"] = childData["caseID"]
    db.update_many(query , {"$set" : {"childData" : childData}})

# 轉錄表 api    
def findDateAndFirstContent(caseID): # argument = caseID , if find return {"dates" : 全部的日期 (type = list) , "FirstContent" : content} , else return False
    db = get_db()
    query = dict()
    query["childData.caseID"] = caseID

    if db.count_documents(query) == 0:
        print("can not find this caseID")
        return False
    
    dates = list()
    data = dict()

    for i in db.find(query):
        dates.append(i["include"]["date"])

    FirstContent = db.find_one(query)["transcribe"]["content"]

    data["dates"] = dates
    data["FirstContent"] = FirstContent
    
    return data

def findContent(caseID , date): # argument = caseID , date , if find return content (type = array) , else return False
    db = get_db()
    query = dict()
    query["childData.caseID"] = caseID
    query["include.date"] = date

    if db.count_documents(query) == 0:
        print("can not find this content")
        return False

    return db.find_one(query)["transcribe"]["content"]

def updateContent(caseID , date , transcriber , content , totalUtterance , validUtterance): # argument = caseID , date , transcriber , content , totalUtterance , validUtterance , if succeed return True , else return False
    db = get_db()
    query = dict()
    query["childData.caseID"] = caseID
    query["include.date"] = date

    if db.count_documents(query) == 0:
        print("can not find this caseID")
        return False

    db.update_one(query , {"$set" : {"transcribe.transcriber" : transcriber , "transcribe.content" : content , "transcribe.totalUtterance" : totalUtterance , "transcribe.validUtterance" : validUtterance}})

    return True

# 彙錄表 api 
def findAnaylsis(caseID , date): # argument = caseID , date , if succeed return anaylsis , else return False
    db = get_db()
    query = dict()
    query["childData.caseID"] = caseID
    query["include.date"] = date

    if db.count_documents(query) == 0:
        print("can not find this anaylsis")
        return False

    return db.find_one(query)["transcribe"]["anaylsis"]

def updateAnaylsis(caseID , date , anaylsis): # argument = caseID , date , anaylsis , if succeed return True , else return False
    db = get_db()
    query = dict()
    query["childData.caseID"] = caseID
    query["include.date"] = date

    if db.count_documents(query) == 0:
        print("can not find this caseID")
        return False

    db.update_one(query , {"$set" : {"transcribe.anaylsis" : anaylsis}})

    return True

objID = ObjectId("607455182078fa7d5e9d01f3")

a1 = {"ID" : "a1" , "role" : "adult" , "utterance" : "1234" , "scenario" : "123"}
a2 = {"ID" : "1" , "role" : "child" , "utterance" : "123" , "scenario" : "123"}
a3 = {"ID" : "" , "role" : "" , "utterance" : "" , "scenario" : "123"}

content = [a1 , a2 , a3]

analysis = {
            'charCount':0,
            'wordCount':0,
            'Content':{
                'N':0,
                'V':0,
                'VH':0,
                'Neu':0,
                'Nf':0,
                'Nh':0,
                'D':0,
                'percentage':0.0,
                'sum':0
            },
            'Function':{
                'P':0,
                'C':0,
                'T':0,
                'I':0,
                'percentage':0.0,
                'sum':0
            },
            'VOCD-w':0.0,
            'VOCD-c':0.0,
            'MLU-w':0,
            'MLU-c':0,
            'MLU5-w':0,
            'MLU5-c':0
        }

date = datetime.datetime.strptime("2018-02-20 00:00", "%Y-%m-%d %H:%M")
birthday = datetime.datetime.strptime("1999-12-24", "%Y-%m-%d")

childData = {"caseID" : "001" , "name" : "1234" , "gender" : "male" , "birthday" : birthday}
include = {"SLP" : "123" , "date" : date}

# print(findDoc("" , "001" , ""))

# print(findChildData("001"))
# upsertDoc(childData , include)

# print(findDateAndFirstContent("001"))
# print(findContent("001" , date))
# updateContent("001" , date , "transcriber" , content)

# print(findAnaylsis("001" , date))
# updateAnaylsis("001" , date , analysis)