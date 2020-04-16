import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

filter_query = { "name" : { "$regex" : "^S"}}

my_doc = mycol.find(filter_query)

for x in my_doc:
    print(x)

