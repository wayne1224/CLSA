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
    global childJoinedDocumentDB
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
        query2Document = dict()

        query2ChildData["caseID"] = caseID
        query2Document["caseID"] = caseID
        query2Document["date"] = date

        if childDataDB.count_documents(query2ChildData) == 0:
            print("Can not find this Child Data")
            return False

        if documentDB.count_documents(query2Document) == 0:
            print("Can not find this Recording")
            return False

        childData = childDataDB.find_one(query2ChildData)
        document = documentDB.find_one(query2Document)

        result = {
            'childData' : childData,
            'document' : document
        }

        return result
        
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
            result[0] = "insert"
            childDataDB.insert_one(childData)
            
        # update
        else: 
            result[0] = "update"
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
        result = ["" , True]

        # insert
        if documentDB.count_documents(query) == 0:
            result[0] = "insert"

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
            result[0] = "update"
            documentDB.update_one(query , {"$set" : {"recording" : recording}})

        return result
    except Exception as e:
        result[1] = False
        print(e)
        return result

def upsertChildDataAndRecording(caseID , date , recording , childData):
    result = ["" , True]
    result1 = upsertChildData(childData)
    result2 = upsertRecording(caseID , date , recording)

    result[0] = result2[0]
    
    if result1[1] == result2[1]:
        if result2[1] == True:
            result[1] = True
        else:
            result[1] = False
    else:
        result[1] = False
    
    return result

# 轉錄表 api
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

# 圖表頁 api
def findChildren(caseID , name): # true : return list 每個 element 都是一個child的dict 他們的document 在 [index]["document"] , false : return false
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
            }
        ])

        result = list(result)
           
        if len(result) == 0:
            return False
                 
        return result
    except Exception as e:
        print(e)
        return False

# childData = {   "caseID" : "00757025",
#                 "name" : "Wayne",
#                 "gender" : "male",
#                 "birthday" : datetime.datetime.strptime("1999-12-24", "%Y-%m-%d")}

# connectDB()
# result = findChildren("12312312" , "")

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


