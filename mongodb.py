# Script to connect to Local Mongo Client on port: 27017 and print some data

import pymongo
from pymongo import MongoClient
client = MongoClient()
db=client['test']
col=db['dataset'].find()
for records in col: 
	print records["_id"]