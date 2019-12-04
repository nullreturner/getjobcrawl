import pymongo

connection = pymongo.MongoClient('localhost', 27017)
db = connection.test
coll = db.Score
docs = coll.find()
for d in docs:
    print(d)


