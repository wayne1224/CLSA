import pymongo
import datetime
import time
import calendar

# CLSA
#     childData
#     document
#          caseID
#          date      
#          recording
#          transcription

# connect to datebase
def connectDB():
    global childDataDB 
    global documentDB 
    client = pymongo.MongoClient()

    try:
        host = "mongodb+srv://wayne1224:wayne1224@sandbox.qjd2q.mongodb.net/myFirstDatabase?authSource=admin&replicaSet=atlas-bu8995-shard-0&w=majority&readPreference=primary&appname=MongoDB%20Compass&retryWrites=true&ssl=true"
        client = pymongo.MongoClient(host , serverSelectionTimeoutMS = 10000) # Timeout 10s
        db = client["CLSA"]         # choose database
        childDataDB = db["childData"] # choose collection
        documentDB = db["document"]   # choose collection
        client.server_info()
        return True

    except Exception as e:
        print(e)
        client.close()
        return False

# 查詢頁 api
def findDocs(SLP , caseID , name):
    try:
        query2ChildData = dict()
        query2Document = dict()       

        # query to childData
        if caseID:
            query["childData.caseID"] = caseID
        if name:
            query["childData.name"] = name

        # query to document
        if SLP:
            query["recording.SLP"] = SLP


        if db.count_documents(query) == 0:
            print("can not find this document")
            return False

        return db.find(query)
    except Exception as e:
        print(e)     

# 收錄表 api
def findChildData(caseID):
    try:
        query = dict()
        query["caseID"] = caseID

        if childDataDB.count_documents(query) == 0:
            print("Can not find this Child Data")
            return False

        return childDataDB.find_one(query)
    except Exception as e:
        print(e)
        return False

def findDoc(caseID , date):
    try:
        query2ChildData = dict()
        query2Recording = dict()

        query2ChildData["caseID"] = caseID
        query2Recording["caseID"] = caseID
        query2Recording["date"] = date

        if childDataDB.count_documents(query2ChildData) == 0:
            print("Can not find this Child Data")
            return False

        if documentDB.count_documents(query2Recording) == 0:
            print("Can not find this Recording")
            return False

        childData = childDataDB.find_one(query2ChildData)
        recording = documentDB.find_one(query2Recording)

        return [childData , recording]
        
    except Exception as e:
        print(e)
        return False

def upsertChildData(childData):
    try:
        query = dict()
        query["caseID"] = childData["caseID"]
        result = ["" , True]

        # insert
        if childDataDB.count_documents(query) == 0:
            childDataID = childDataDB.insert_one(childData).inserted_id
            result[0] = childDataID

        # update
        else: 
          childDataDB.update_many(query , {"$set" : {
                                                        "caseID" : childData["caseID"],
                                                        "name" : childData["name"],
                                                        "gender" : childData["gender"],
                                                        "birthday" : childData["birthday"]
                                                        }})
        
        return result
    except Exception as e:
        result[1] = False
        print(e) 
        return result

def upsertRecording(caseID , date , recording):
    try:
        query = dict()
        query["caseID"] = caseID
        query["date"] = date

        # insert
        if documentDB.count_documents(query) == 0:
            data = {
                "caseID" : caseID, 
                "date" : date,
                "recording" : recording,
                "transcription" : { "transcriber" : None, 
                                    "content" : None,
                                    "analysis" : None,
                                    "totalUtterance" : None,
                                    "validUtterance" : None
                } 
            }
            
            documentDB.insert_one(data)
        # update
        else:
            documentDB.update_one(query , {"$set" : {"recording" : recording}})

    except Exception as e:
        print(e)

# 轉錄表 api
def findDatesAndFirstContent(caseID):
    try:
        dates = list()
        query = dict()
        query["caseID"] = caseID

        if documentDB.count_documents(query) == 0:
            print("can not find this caseID")
            return False
  
        for i in documentDB.find(query):
            dates.append(i["date"])
        
        data = documentDB.find_one(query)["transcription"]

        result = dict()
        result["dates"] = dates
        result["transcriber"] = data["transcriber"]
        result["FirstContent"] = data["content"]

        return result

    except Exception as e:
        print(e)
        return False

def findContent(caseID , date):
    try:
        query = dict()
        query["caseID"] = caseID
        query["date"] = date

        if documentDB.count_documents(query) == 0:
            print("can not find this content")
            return False
        
        data = documentDB.find_one(query)["transcription"]

        result = dict()
        result["transcriber"] = data["transcriber"]
        result["FirstContent"] = data["content"]

        return result

    except Exception as e:
        print(e)

def updateContent(caseID , date , transcriber , content , totalUtterance , validUtterance):
    try:
        query = dict()
        query["caseID"] = caseID
        query["date"] = date

        if documentDB.count_documents(query) == 0:
            print("can not find this caseID or date")
            return False
        
        try:
            documentDB.update_one(query , {"$set" : {
                                            "transcription.transcriber" : transcriber , 
                                            "transcription.content" : content , 
                                            "transcription.totalUtterance" : totalUtterance , 
                                            "transcription.validUtterance" : validUtterance}})
            return True
        except pymongo.errors.PyMongoError as e:
            return False
    except Exception as e:
        print(e)
        return False

# 彙錄表 api
def findAnalysis(caseID , date):
    try:
        query = dict()
        query["caseID"] = caseID
        query["date"] = date

        if documentDB.count_documents(query) == 0:
            print("can not find this analysis")
            return False
        
        return documentDB.find_one(query)["transcription"]["analysis"]
    except Exception as e:
        print(e)
        return False

def updateAnalysis(caseID , date , analysis):
    try:
        query = dict()
        query["caseID"] = caseID
        query["date"] = date

        if documentDB.count_documents(query) == 0:
            print("can not find this caseID or date")
            return False

        try:
            documentDB.update_one(query , {"$set" : {"transcription.analysis" : analysis}})
            return True
        except pymongo.errors.PyMongoError as e:
            return False

    except Exception as e:
        print(e)
        return False

# childData = {   "caseID" : "00757025",
#                 "name" : "Wayne",
#                 "gender" : "male",
#                 "birthday" : datetime.datetime.strptime("1999-12-24", "%Y-%m-%d")}

# connectDB()

# print(upsertChildData(childData))
# upsertRecording("00757025" , datetime.datetime.strptime("2021-07-15", "%Y-%m-%d") , "Recording2")
# print(findChildData("00757025"))
# print(findDoc("00757025" , datetime.datetime.strptime("2021-07-15", "%Y-%m-%d")))

        