import pymongo
from pymongo import MongoClient

client=MongoClient("mongodb://127.0.0.1:27017")

db=client['PROJECT']

coll=db.details

def mg(fname,lname,uname,email,password):
    coll.insert_one({"fname":fname,"lname":lname,"uname":uname,"email":email,"password":password})

def check_it(email):
    list=coll.find_one({"email":email})
    return list
