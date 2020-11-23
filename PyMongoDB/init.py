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

userDict = {
    'name': 'Clever Cracker',
    'address': 'Local Address',
    'age': 33,
    'hobby': ['Programming', 'Coding', 'Thinking']
}

userDictNew = {
    'name': 'Clever Cracker',
    'address': 'Local Address',
    'age': 33,
    'hobby': ['Programming', 'Coding', 'Thinking']
}
x = testCollection.insert_one(userDictNew)
x.inserted_id
mylist = [
    {"name": "Amy", "address": "Apple st 652"},
    {"name": "Hannah", "address": "Mountain 21"},
    {"name": "Michael", "address": "Valley 345"},
    {"name": "Sandy", "address": "Ocean blvd 2"},
    {"name": "Betty", "address": "Green Grass 1"},
    {"name": "Richard", "address": "Sky st 331"},
    {"name": "Susan", "address": "One way 98"},
    {"name": "Vicky", "address": "Yellow Garden 2"},
    {"name": "Ben", "address": "Park Lane 38"},
    {"name": "William", "address": "Central st 954"},
    {"name": "Chuck", "address": "Main Road 989"},
    {"name": "Viola", "address": "Sideway 1633"}
]

testCollection.insert_many(mylist)
