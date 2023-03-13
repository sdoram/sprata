
from pymongo import MongoClient
client = MongoClient('mongodb+srv://sparta:sparta@cluster0.ahs6lya.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

doc = {'name':'bobby','age':21}
db.users.insert_one(doc)