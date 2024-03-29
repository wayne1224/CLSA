import pymongo
import subprocess
import os
# CLSA
#     childData
#     document
#          caseID
#          date      
#          recording
#          transcription
#     norm

# 第一次開啟軟體時，MongoDB 內尚無 database 和 collection，所以需要此 function 做 initial，創建 database 和 collection
def initialDB():
    # Check collections exist
    
    db = client["CLSA"]
    
    if "norm" not in db.list_collection_names():
        normDB = db['norm']
        ageCh = ["二歲" , "二歲半" , "三歲" , "三歲半" , "四歲" , "四歲半" , "五歲" , "五歲半" , "六歲" , "六歲半" , "七歲" , "七歲半" , "八歲" , "八歲半" , "九歲" , "九歲半" , "十歲" , "十歲半" , "十一歲" , "十一歲半" , "十二歲"]
        ageNum = [2 , 2.5 , 3 , 3.5 , 4 , 4.5 , 5 , 5.5 , 6 , 6.5 , 7 , 7.5 , 8 , 8.5 , 9 , 9.5 , 10 , 10.5 , 11 , 11.5 , 12]

        data = list()

        for i in range(len(ageCh)):
            data.append({
                "age" : ageCh[i],
                "ageNum" : ageNum[i],
                "data" : {
                    "mlu-c" : 0.0,
                    "mlu-w" : 0.0,
                    "vocd-c" : 0.0,
                    "vocd-w" : 0.0
                },
                "base": {
                    "mlu": 0,
                    "vocd": 0
                }
            })
            
        result = normDB.insert_many(data)
        while result.acknowledged != True: #防止沒寫進就crash
            continue
    
    if "childData" not in db.list_collection_names():
        childDataDB = db['childData']
        childDataDB.insert_one({"for initial" : True})
        childDataDB.delete_one({"for initial" : True})

    if "document" not in db.list_collection_names():
        documentDB = db['document']
        documentDB.insert_one({"for initial" : True})
        documentDB.delete_one({"for initial" : True})


# connect to datebase
def connectDB():
    global childDataDB 
    global documentDB
    global normDB
    global settingDB
    global client
    global server

    try: 
        subprocess.call(["mongodb_dir.bat"])
        # Check Database path exists
        path = "C:/data/db"
        if not os.path.isdir(path):
            os.makedirs(path)

        server = subprocess.Popen("C:/Program Files/MongoDB/Server/5.0/bin/mongod.exe")
        client = pymongo.MongoClient('localhost', 27017) 
        initialDB()
        #mongoDB_server = subprocess.Popen("C:/Program Files/MongoDB/Server/5.0/bin/mongod.exe")
         # Timeout 10s
        db = client["CLSA"]           # choose database
        childDataDB = db["childData"] # choose collection
        documentDB = db["document"]   # choose collection   
        normDB = db["norm"]           # choose collection  
        settingDB = db["setting"]     # choose collection  
        client.server_info()
        return True

    except Exception as e:
        print(e)
        client.close()
        return False

def close_mongodb():
    server.kill()

# 查詢頁 api
def findDocs(SLP , caseID , name):
    try:
        query = dict()
        
        if caseID:
            query["caseID"] = caseID
        if name:
            query["childData.name"] = name
        if SLP:
            query["recording.SLP"] = SLP

        
        result = documentDB.aggregate([
            {
                '$lookup': {
                    'from': 'childData', 
                    'localField': 'caseID', 
                    'foreignField': 'caseID', 
                    'as': 'childData'
                }
            }, {
                '$project': {
                    'caseID': 1, 
                    'date': 1, 
                    'recording': 1, 
                    'transcription': 1, 
                    'childData': {
                        '$arrayElemAt': [
                            '$childData', 0
                        ]
                    }, 
                    'otherField': 1
                }
            }, {
                '$match': query
            },
            {
                '$sort': {
                    'caseID': 1, 
                    'date': 1
                }
            }
        ])

        # for i in list(result):
        #     print(i)

        return result
    except Exception as e:
        print(e)     

def deleteDoc(objID): # 只刪除document 不刪除childData
    try:
        query = dict()
        query["_id"] = objID

        before = len(list(documentDB.find()))
        documentDB.delete_one(query)
        after = len(list(documentDB.find()))

        if before > after: 
            return True
        else:
            return False
    except Exception as e:
        print(e) 

# 收錄表 api
def findChildData(caseID): # return child Data (not include object ID) or False
    try:
        query = dict()
        query["caseID"] = caseID
        
        # 找不到 child data , return False
        if childDataDB.count_documents(query) == 0:
            print("can not find this Child Data")
            return False

        # 找到 child data , return child data
        else:
            data = childDataDB.find_one(query)
            del data['_id']
            return data

    except Exception as e:
        print("The error of function findChildData() !!")
        print(e)
        return False

def findDocument(caseID , date): # return boolean
    try:
        query = dict()
        query["caseID"] = caseID
        query["date"] = date

        # 找不到 document , return False
        if documentDB.count_documents(query) == 0:
            print("can not find this Child Data")
            return False

        # 找到 document , return True
        else:
            return True

    except Exception as e:
        print("The error of function findDocument() !!")
        print(e)
        return False

def canInsertDoc(caseID , date): # return boolean , if error return None
    # check caseID and date
    try:
        query = dict()
        query["caseID"] = caseID
        query["date"] = date

        # 有找到 代表有重複 doc , return False => 不能新增
        if documentDB.count_documents(query) != 0:
            return False

        # 沒找到 代表無重複 doc , return True => 可以新增
        else:
            return True
             
    except Exception as e:
        print("The error of function canInsertDoc() !!")
        print(e)
        return None

def canUpdateDoc(caseID , date , documentID): # return boolean , if error return None
    # check caseID , date and document ID
    try:
        query = dict()
        query["caseID"] = caseID
        query["date"] = date

        # 有找到 代表有重複 doc
        if documentDB.count_documents(query) != 0:
            data = documentDB.find_one(query)

            # 是同一個 doc , return True => 可以更新
            if data["_id"] == documentID:
                return True
            
            # 不同的 doc , return False => 不能更新
            else:
                return False

        # 沒找到 代表無重複 doc , return True => 可以更新
        else:
            return True
             
    except Exception as e:
        print("The error of function canUpdateDoc() !!")
        print(e)
        return None

## insert update 合併
def upsertChildData(childData): # insert => child data object ID / update => boolean
    try:
        # update child data
        if findChildData(childData["caseID"]):
            query = dict()
            query["caseID"] = childData["caseID"]

            childDataDB.update_many(query , {"$set" : {                                                       
                                                            "name" : childData["name"],
                                                            "gender" : childData["gender"],
                                                            "birthday" : childData["birthday"]
                                                            }})

            return True
        # insert child data
        else:
            return childDataDB.insert_one(childData).inserted_id

        # # insert child data
        # if upsert == "insert":
        #     # 此 child 已經在資料庫裡了 , return False => 不能新增 
        #     if findChildData(childData["caseID"]):
        #         print("This case ID already exists and can not insert to database !!")
        #         return False

        #     # 此 child 沒有在資料庫裡了 , return object ID => 可以新增 
        #     else:
        #         return childDataDB.insert_one(childData).inserted_id
                
        # # update child data
        # elif upsert == "update":
        #     query = dict()
        #     query["caseID"] = childData["caseID"]

        #     # 在 child data 裡，找不到這個個案 , return False 
        #     if documentDB.count_documents(query) == 0:
        #         print("can not find this child data !!")
        #         return False
            
        #     # 在 child data 裡，找到這個個案，並且更改 , return True
        #     else:
        #         childDataDB.update_many(query , {"$set" : {                                                       
        #                                                     "name" : childData["name"],
        #                                                     "gender" : childData["gender"],
        #                                                     "birthday" : childData["birthday"]
        #                                                     }})

        #         return True

    except Exception as e:
        print("The error of function upsertChildData() !!")
        print(e)     
        return False

def insertChildData(childData): # return object ID or False
    try:
        # 此 child 已經在資料庫裡了 , return False => 不能新增 
        if findChildData(childData["caseID"]):
            print("This case ID already exists and can not insert to database !!")
            return False

        # 此 child 沒有在資料庫裡了 , return object ID => 可以新增 
        else:
            return childDataDB.insert_one(childData).inserted_id

    except Exception as e:
        print("The error of function insertChildData() !!")
        print(e)     
        return False

def updateChildData(childData): # return boolean
    try:
        query = dict()
        query["caseID"] = childData["caseID"]

        # 在 child data 裡，找不到這個個案 , return False 
        if documentDB.count_documents(query) == 0:
            print("can not find this child data !!")
            return False
        
        # 在 child data 裡，找到這個個案，並且更改 , return True
        else:
            childDataDB.update_many(query , {"$set" : {                                                       
                                                        "name" : childData["name"],
                                                        "gender" : childData["gender"],
                                                        "birthday" : childData["birthday"]
                                                        }})

            return True
    except Exception as e:
        print("The error of function updateChildData() !!")
        print(e) 
        return False

def insertRecording(caseID , date , recording): #0 return boolean
    try:
        # 此 document 已經在資料庫裡了 , return False => 不能新增 
        if findDocument(caseID , date):
            print("This case ID and date already exists and can not insert to database !!")
            return False

        # 此 document 沒有在資料庫裡了 , return object ID => 可以新增 
        else:
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
            
            return documentDB.insert_one(data).inserted_id

    except Exception as e:
        print("The error of function insertRecording() !!")
        print(e)
        return False

def updateRecording(documentID , caseID , date , recording): # return boolean 
    try:
        query = dict()
        query["_id"] = documentID

        # 在 document 裡，找不到這個個案 , return False => 不能更新
        if documentDB.count_documents(query) == 0:
            print("can not find this document!!")
            return False
        
        # 在 document 裡，找到這個個案 , return True => 可以更新
        else:
            documentDB.update_one(query , {"$set" : {
                                                        "caseID" : caseID,
                                                        "date" : date,
                                                        "recording" : recording
                                                        }})

            return True
    except Exception as e:
        print("The error of function updateRecording() !!")
        print(e)   
        return False

# 轉錄表 api
def findContent(documentID): # return transcription or False
    try:
        query = dict()
        query["_id"] = documentID

        if documentDB.count_documents(query) == 0:
            print("Can not find this content")
            return False
        
        data = documentDB.find_one(query)["transcription"]

        result = dict()
        result["transcriber"] = data["transcriber"]
        result["FirstContent"] = data["content"]

        return result

    except Exception as e:
        print(e)

def updateContent(documentID , transcriber , content , totalUtterance , validUtterance): # return boolean
    try:
        query = dict()
        query["_id"] = documentID

        # 找不到 doc , return False => 無法更新 content 
        if documentDB.count_documents(query) == 0:
            print("can not find this document")
            return False

        # 找到 doc , return True => 可以更新 content 
        else:
            documentDB.update_one(query , {"$set" : {
                                            "transcription.transcriber" : transcriber, 
                                            "transcription.content" : content, 
                                            "transcription.totalUtterance" : totalUtterance, 
                                            "transcription.validUtterance" : validUtterance
                                            }})

        return True


    except Exception as e:
        print("The error of function updateContent() !!")
        print(e)
        return False

# 彙錄表 api
def updateAnalysis(documentID , analysis): # return boolean
    try:
        query = dict()
        query["_id"] = documentID

        # 找不到 doc , return False => 無法更新 analysis
        if documentDB.count_documents(query) == 0:
            print("can not find this document")
            return False

        # 找不到 doc , return False => 無法更新 analysis
        else:
            documentDB.update_one(query , {"$set" : {"transcription.analysis" : analysis}})
            return True
    
    except Exception as e:
        print("The error of function updateAnalysis() !!")
        print(e)
        return False

# 圖表頁 api
def findChildren(caseID , name): 
    # find : return list 
    # 每個 element 都是一個 child(type == dict) 
    # 他們的 document(type == list) 在 child[i]["document"]  
    # 若要 access document 中的資料 child[i]["document"][j] 
    # not find : return false

    try:  
        query = dict()

        if caseID:
            query["caseID"] = caseID
        if name:
            query["name"] = name

        result = childDataDB.aggregate([
            {
                '$lookup': {
                    'from': 'document', 
                    'localField': 'caseID', 
                    'foreignField': 'caseID', 
                    'as': 'document'
                }
            }, 
            {
                '$match': query
            }, 
            {
                '$unwind': {
                    'path': '$document'
                }
            }, 
            {
                '$sort': {
                    'document.date': 1
                }
            }, 
            {
                '$group': {
                    '_id': '$_id', 
                    'name': {
                        '$first': '$name'
                    }, 
                    'caseID': {
                        '$first': '$caseID'
                    }, 
                    'gender': {
                        '$first': '$gender'
                    }, 
                    'birthday': {
                        '$first': '$birthday'
                    }, 
                    'document': {
                        '$push': '$document'
                    }
                }
            },
            {
                '$project': {
                    'name': 1, 
                    'caseID': 1, 
                    'gender': 1, 
                    'birthday': 1, 
                    'document': 1, 
                    'length': {
                        '$size': '$document'
                    }
                }
            }, 
            {
                '$sort': {
                    'length': -1
                }
            }
        ])
                          
        return result
    except Exception as e:
        print(e)
        return False

def updateNorm(ageNum , data , base):
    try:
        query = dict()
        query["ageNum"] = ageNum
    
        normDB.update_one(query , {"$set" : {
                                                "data" : data,
                                                "base" : base
                                            }}) 


        return True
    except Exception as e:
        print(e)
        return False

def deleteNorm(age): # age是中文
    try:
        query = dict()
        query["age"] = age
        
        if normDB.count_documents(query) == 0:
            print("can not find this content")
            return False
        
        normDB.delete_one(query)
        return True

    except Exception as e:
        print(e)
        return False

def findNormByAge(age): # age是中文
    try:
        query = dict()
        query["age"] = age
        
        if normDB.count_documents(query) == 0:
            print("can not find this content")
            return False
        
        return normDB.find_one(query)

    except Exception as e:
        print(e)
        return False

def findClosestNorm(ageNum): ## 往前找最近的年齡檔案
    try:
        data = normDB.find().sort("ageNum")
        data = list(data)
        
        while True:
            for doc in reversed(data):
                if doc["ageNum"] == ageNum and (doc["data"]["mlu-c"] or doc["data"]["mlu-w"] or doc["data"]["vocd-c"] or doc["data"]["vocd-w"]):
                    return doc

            ageNum = ageNum - 0.5

            if ageNum == 0:
                return False

    except Exception as e:
        print(e)
        return False

def findVOCD(ageNum): # ageNum = list()
    try:
        data = normDB.find().sort("ageNum")
        data = list(data)
        result = list()

        for age in ageNum:
            for norm in data:
                if norm["ageNum"] == age:
                    tmp = dict()
                    tmp["vocd-c"] = norm["data"]["vocd-c"]
                    tmp["vocd-w"] = norm["data"]["vocd-w"]
                    result.append(tmp)
                    break
        
        return result

    except Exception as e:
        print("The error of function findVOCD() !!")
        print(e)
        return False

def findMLU(ageNum): # ageNum = list()
    try:
        data = normDB.find().sort("ageNum")
        data = list(data)
        result = list()

        for age in ageNum:
            for norm in data:
                if norm["ageNum"] == age:
                    tmp = dict()
                    tmp["mlu-c"] = norm["data"]["mlu-c"]
                    tmp["mlu-w"] = norm["data"]["mlu-w"]
                    result.append(tmp)
                    break
        
        return result

    except Exception as e:
        print("The error of function findMLU() !!")
        print(e)
        return False

def getNormAges():
    try:
        return normDB.find().sort("ageNum")
    except Exception as e:
        print(e)
        return False

# 輸入輸出資料
# caseID 重複加數字 ex : 00757025 => 00757025(1)
# norm 直接取代
def importCLSA(childData , document , norm):  
    from datetime import datetime

    try:
        for c in childData:
            # 此 child 已經在資料庫裡了 
            c["birthday"] = datetime.strptime(c["birthday"] , "%Y-%m-%d %H:%M:%S")
                   
            if childDataDB.find_one({"caseID" : c["caseID"]}):
                # caseID + (數字) => ex: 00757025 , 00757025(1) , 00757025(2) , 00757025(3) ,,,
                copy = 1
                
                while(childDataDB.find_one({"caseID" : c["caseID"] + "({})".format(copy)})):
                    copy = copy + 1
                
                childDataDB.insert_one({
                    "caseID" : c["caseID"] + "({})".format(copy),
                    "name" : c["name"],
                    "gender" : c["gender"],
                    "birthday" : c["birthday"]  # 2010-01-07 00:00:00
                })

                # 將 document 的 caseID 做更改 => ex : 原本 caseID = 00757025 , 但經過上方的程式變成 00757025(1) , document 裡的 caseID 也要更改
                for i in range(len(document)):
                    if document[i]["caseID"] == c["caseID"]:
                        document[i]["caseID"] = c["caseID"] + "({})".format(copy)
                
            # 此 child 沒有在資料庫裡了
            else:
                childDataDB.insert_one(c)

    except Exception as e:
        print("The error of function importCLSA.importChildData !!")   
        print(e)
        return False  

    # import document
    try:
        for d in document:
            d["date"] = datetime.strptime(d["date"] , "%Y-%m-%d %H:%M:%S")
            
            documentDB.insert_one(d)
    except Exception as e:
        print("The error of function importCLSA.importDocument !!")   
        print(e)
        return False 

    # import norm
    try:
        for n in norm:
            query = {"age" : n["age"]}
            normDB.update_one(query , {"$set" : {"data" : n["data"] , "base" : n["base"]}})

    except Exception as e:
        print("The error of function importCLSA.importNorm !!")   
        print(e)
        return False 
    
    return True

def importNorm(norm):
    try:
        for n in norm:
            query = {"age" : n["age"]}
            normDB.update_one(query , {"$set" : {"data" : n["data"] , "base" : n["base"]}})
    except Exception as e:
        print("The error of function importCLSA.importNorm !!")   
        print(e)
        return False
       
    return True
     
def exportCLSA():
    try:
        childData = list(childDataDB.aggregate([{'$project': {'_id': 0}}]))
        document = list(documentDB.aggregate([{'$project': {'_id': 0}}]))
        norm = list(normDB.aggregate([{'$project': {'_id': 0}}]))

        for i in range(len(childData)):
            childData[i]["birthday"] =  childData[i]["birthday"].strftime("%Y-%m-%d %H:%M:%S")
        
        for i in range(len(document)):
            document[i]["date"] =  document[i]["date"].strftime("%Y-%m-%d %H:%M:%S")

        result = {
            "childData" : childData,
            "document" : document,
            "norm" : norm
        }

        return result

    except Exception as e:
        print(e)
        return False

def exportNorm():
    try:
        return list(normDB.aggregate([{'$project': {'_id': 0}}]))

    except Exception as e:
        print(e)
        return False

def deleteAll():
    try:
        childDataDB.delete_many({})
        documentDB.delete_many({})
    except Exception as e:
        print("The error of function deleteAll !!")   
        print(e)

# connectDB()
# deleteAll()
