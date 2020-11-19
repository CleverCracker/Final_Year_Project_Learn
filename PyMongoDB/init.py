import pymongo
from pymongo import MongoClient

localClient = MongoClient('mongodb://localhost:27017/')

testDB = localClient['testDB']

dbList = localClient.list_database_names()

if 'testDB' in dbList:
    print('DB FOUND...')

testDB.list_collection_names()

testCollection = testDB['test_collection']

collectionList = testDB.list_collection_names()
if 'test_collection' in collectionList:
    print('Collection is Exits')
