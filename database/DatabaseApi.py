import pymongo
import subprocess
# CLSA
#     setting
#     childData
#     document
#          caseID
#          date      
#          recording
#          transcription
#     norm

# 第一次開啟軟體時，MongoDB 內尚無 database 和 collection，所以需要此 function 做 initial，創建 database 和 collection
def intialDB():
    host = "mongodb://wayne1224:wayne1224@sandbox-shard-00-00.qjd2q.mongodb.net:27017,sandbox-shard-00-01.qjd2q.mongodb.net:27017,sandbox-shard-00-02.qjd2q.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-bu8995-shard-0&authSource=admin&retryWrites=true&w=majority"
    client = pymongo.MongoClient(host , serverSelectionTimeoutMS = 10000, ssl=True, ssl_cert_reqs='CERT_NONE') # Timeout 10s 
      
    db = client["CLSA"]  
    childDataDB = db['childData']
    documentDB = db['document']
    normDB = db['norm']
    settingDB = db['setting']

    childDataDB.insert_one({"for initial" : True})
    documentDB.insert_one({"for initial" : True})
    normDB.insert_one({"for initial" : True})
    settingDB.insert_one({"for initial" : True})

# connect to datebase
def connectDB():
    global childDataDB 
    global documentDB
    global normDB
    global settingDB

    try:
        subprocess.Popen("C:/Program Files/MongoDB/Server/5.0/bin/mongod.exe")
        client = pymongo.MongoClient('localhost', 27017)  # Timeout 10s
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

        result = list(result)
           
        if len(result) == 0:
            return False
                 
        return result
    except Exception as e:
        print(e)
        return False

def updateNorm(ageNum , data):
    try:
        query = dict()
        query["ageNum"] = ageNum
    
        normDB.update_one(query , {"$set" : {
                                                "data" : data
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

# setting api
def isFieldSurvey():
    try:
        query = dict()
        query["mode"] = "fieldSurvey"

        return settingDB.find_one(query)["state"]

    except Exception as e:
        print("The error of function isFieldSurvey() !!")
        print(e)
        return False

def changeModeState(state):
    try:
        query = dict()
        query["mode"] = "fieldSurvey"

        settingDB.update_one(query , {"$set" : {
                                                "state" : state
                                            }}) 

        return True

    except Exception as e:
        print("The error of function changeModeState() !!")
        print(e)
        return False


# childData = {   "caseID" : "00757025",
#                 "name" : "Wayne",
#                 "gender" : "male",
#                 "birthday" : datetime.datetime.strptime("1999-12-24", "%Y-%m-%d")}

# data = {
#     "VOCD-a" : 123,
#     "VOCD-b" : 456
# }

# connectDB()
# upsertNorm("2" , data)

# print(result)
# for i in result:
#     print(i)

# findDocs return
# [
#     {
#         '_id': ObjectId('60f3f8cbefb5822f048b2bac'), 
#         'caseID': '00757045', 
#         'date': datetime.datetime(2021, 7, 18, 17, 42, 24), 
#         'recording': {
#             'date': datetime.datetime(2021, 7, 18, 17, 42, 24), 
#             'SLP': '丁信志', 
#             'scenario': '下午', 
#             'fileName': 'sun in 7', 
#             'location': '虎尾', 
#             'interactionType': '自由遊戲', 
#             'inducement': 'NBA', 
#             'participants': ['兒童', '爸 爸', '媽媽'], 
#             'equipment': '錄音筆', 
#             'help': '有時 (2~5次)', 
#             'others': '無', 
#             'situation': '無'
#             }, 
#         'transcription': {
#             'transcriber': None, 
#             'content': None, 
#             'analysis': None, 
#             'totalUtterance': None, 
#             'validUtterance': None}, 
#         'childData': {
#             '_id': ObjectId('60f3f8cbefb5822f048b2bab'), 
#             'caseID': '00757045', 
#             'name': 'Kenneth', 
#             'gender': 'male', 
#             'birthday': datetime.datetime(2000, 1, 5, 0, 0)
#         }
#     }
# ]

# findDoc return
# {'childData': {
#     '_id': ObjectId('60f0079855497c379424380c'), 
#     'caseID': '00757025', 
#     'name': 'Wayne', 
#     'gender': 'male', 
#     'birthday': datetime.datetime(1999, 12, 24, 0, 0)
#     }, 
# 'document': {
#     '_id': ObjectId('60f2a9308cf2f71f708dc0d6'), 
#     'caseID': '00757025', 
#     'date': datetime.datetime(2021, 7, 15, 0, 0), 
#     'recording': {
#         'date': datetime.datetime(2021, 5, 10, 19, 11, 47), 
#         'SLP': '何文子', 
#         'scenario': '晚上', 
#         'fileName': 'CC', 
#         'location': '海大', 
#         'interactionType': '自由遊戲', 
#         'inducement': '健身咖', 
#         'participants': ['兒童', '老師', 'test'], 
#         'equipment': '攝影機', 'help': '經常 (6~9次)', 
#         'others': '健身', 
#         'situation': ''}, 
#     'transcription': {
#         'transcriber': None, 
#         'content': None, 
#         'analysis': None, 
#         'totalUtterance': None, 
#         'validUtterance': None}
#         }
# }


