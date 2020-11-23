from pymongo import MongoClient

myClient = MongoClient('mongodb://localhost:27017/')
myClient.list_database_names()

testDB = myClient['testDB']
testDB.list_collection_names()
testCollection = testDB['test_collection']
x = testCollection.find()

for x in testCollection.find({'name': 'Clever Cracker'}):
    print(x)
