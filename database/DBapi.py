import pymongo
import datetime
import time
import calendar

# connect to datebase
def connectDB():
    global CLSA  
    client = pymongo.MongoClient()

    try:
        host = "mongodb+srv://wayne1224:wayne1224@sandbox.qjd2q.mongodb.net/myFirstDatabase?authSource=admin&replicaSet=atlas-bu8995-shard-0&w=majority&readPreference=primary&appname=MongoDB%20Compass&retryWrites=true&ssl=true"
        client = pymongo.MongoClient(host , serverSelectionTimeoutMS = 10000) # Timeout 10s
        db = client["Test"] # choose database
        CLSA = db["CLSA"] # choose collection
        client.server_info()
        return True

    except Exception as e:
        print(e)
        client.close()
        return False

# 查詢頁 api
def findDocs(SLP , caseID , name): # argument = SLP , caseID , name, if find return pymongo object , else return False
    try:
        db = CLSA
        query = dict()

        if SLP:
            query["recording.SLP"] = SLP
        if caseID:
            query["childData.caseID"] = caseID
        if name:
            query["childData.name"] = name

        if db.count_documents(query) == 0:
            print("can not find this document")
            return False

        return db.find(query)
    except Exception as e:
        print(e)

def deleteDoc(objID): # argument = caseID , date , if delete successfully return True , else return False
    try:
        db = CLSA
        query = dict()
        query["_id"] = objID

        before = len(list(db.find()))
        db.delete_one(query)
        after = len(list(db.find()))

        if before > after: 
            return True
        else:
            return False
    except Exception as e:
        print(e)    

# 收錄表 api
def findChildData(caseID): # argument = caseID , if find return childData (type = dict) , else return False
    try:
        db = CLSA
        query = dict()
        query["childData.caseID"] = caseID

        if db.count_documents(query) == 0:
            print("can not find this caseID")
            return False

        return db.find_one(query)["childData"]
    except Exception as e:
        print(e)

def findDoc(caseID , date): # argument = caseID , date , if find return document , else return False
    try:
        db = CLSA
        query = dict()
        query["childData.caseID"] = caseID
        query["recording.date"] = date 

        if db.count_documents(query) == 0:
            print("can not find this doc")
            return False

        return db.find_one(query)
    except Exception as e:
        print(e)

def upsertChildDataAndRecording(childData , recording): # argument = childData , recording , if upsert successfully return [("insert" or "update") , True]
    try:
        db = CLSA
        query = dict()
        query["childData.caseID"] = childData["caseID"]
        query["recording.date"] = recording["date"]  

        result = ["" , True]

        # 更新收錄表
        if db.count_documents(query) != 0: 
            result[0] = "update"

            try:
                db.update_one(query , {"$set" : {"childData" : childData , "recording" : recording}})
                result[1] = True
            except pymongo.errors.PyMongoError as e:
                result[1] = False
            
        # 插入新的收錄表  
        else:
            result[0] = "insert"
            
            data = {
                "childData" : childData,
                "recording" : recording,
                "transcription" : {"transcriber" : None, 
                                "content" : None,
                                "analysis" : None,
                                "totalUtterance" : None,
                                "validUtterance" : None
                } 
            }

            before = len(list(db.find()))
            db.insert_one(data)
            after = len(list(db.find()))

            if before < after: 
                result[1] = True
            else:
                result[1] = False
            
        # 更新舊的childData
        if result[1]:
            query = dict()
            query["childData.caseID"] = childData["caseID"]
            db.update_many(query , {"$set" : {"childData" : childData}})
        
        return result
    except Exception as e:
        print(e)

# 轉錄表 api    
def findDateAndFirstContent(caseID): # argument = caseID , if find return {"dates" : 全部的日期 (type = list) , "FirstContent" : content} , else return False
    try:
        db = CLSA
        query = dict()
        query["childData.caseID"] = caseID

        if db.count_documents(query) == 0:
            print("can not find this caseID")
            return False
        
        dates = list()
        
        for i in db.find(query):
            dates.append(i["recording"]["date"])

        data = db.find_one(query)["transcription"]

        result = dict()
        result["dates"] = dates
        result["transcriber"] = data["transcriber"]
        result["FirstContent"] = data["content"]
        
        return result
    except Exception as e:
        print(e)

def findContent(caseID , date): # argument = caseID , date , if find return content (type = array) , else return False
    try:
        db = CLSA
        query = dict()
        query["childData.caseID"] = caseID
        query["recording.date"] = date

        if db.count_documents(query) == 0:
            print("can not find this content")
            return False

        data = db.find_one(query)["transcription"]

        result = dict()
        result["transcriber"] = data["transcriber"]
        result["FirstContent"] = data["content"]

        return result
    except Exception as e:
        print(e)

def updateContent(caseID , date , transcriber , content , totalUtterance , validUtterance): # argument = caseID , date , transcriber , content , totalUtterance , validUtterance , if succeed return True , else return False
    try:
        db = CLSA
        query = dict()
        query["childData.caseID"] = caseID
        query["recording.date"] = date

        if db.count_documents(query) == 0:
            print("can not find this caseID or date")
            return False

        try:
            db.update_one(query , {"$set" : {"transcription.transcriber" : transcriber , "transcription.content" : content , "transcription.totalUtterance" : totalUtterance , "transcription.validUtterance" : validUtterance}})
            return True
        except pymongo.errors.PyMongoError as e:
            return False
    except Exception as e:
        print(e)

# 彙錄表 api 
def findAnalysis(caseID , date): # argument = caseID , date , if succeed return analysis , else return False
    try:
        db = CLSA
        query = dict()
        query["childData.caseID"] = caseID
        query["recording.date"] = date

        if db.count_documents(query) == 0:
            print("can not find this analysis")
            return False

        return db.find_one(query)["transcription"]["analysis"]
    except Exception as e:
        print(e)

def updateAnalysis(caseID , date , analysis): # argument = caseID , date , analysis , if succeed return True , else return False
    try:
        db = CLSA
        query = dict()
        query["childData.caseID"] = caseID
        query["recording.date"] = date

        if db.count_documents(query) == 0:
            print("can not find this caseID or date")
            return False

        try:
            db.update_one(query , {"$set" : {"transcription.analysis" : analysis}})
            return True
        except pymongo.errors.PyMongoError as e:
            return False
    except Exception as e:
        print(e)


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

date = datetime.datetime.strptime("2021-04-26 00:00", "%Y-%m-%d %H:%M")
birthday = datetime.datetime.strptime("1999-12-24", "%Y-%m-%d")

childData = {"caseID" : "001" , "name" : "1234" , "gender" : "male" , "birthday" : birthday}
recording = {"SLP" : "123" , "date" : date}

# connectDB()

# print(findDocs("" , "001" , ""))
# print(deleteDoc("165497489"))

# print(findChildData("001"))
# print(findChildDataAndRecording("00757001" , date))
# print(upsertChildAndInclude(childData , recording))

# print(findDateAndFirstContent("001"))
# print(findContent("001" , date))
# print(updateContent("test6" , date , "transcriber" , content , 10 , 8))

# print(findAnalysis("001" , date))
# updateAnalysis("001" , date , analysis)