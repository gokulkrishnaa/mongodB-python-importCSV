import os, pprint, csv
from pymongo import MongoClient

client=MongoClient()
db=client['newest']

def file_csv(file,name):
	with open(file,'rb') as csvfile:
		parse=csv.DictReader(csvfile, delimiter=',', quotechar='"', skipinitialspace=True)
		for data in parse:
			import_to_mongo(data,name)

def import_to_mongo(data,name):
	col=db[name]
	# print "importing"
	# col.insert(data)
	# print "imported"


path="/Users/GK/Downloads/dataset/dataset/app_usage"
files = os.listdir(path)
i=1
for file in files:
	file_csv(path+"/"+file,file)
	break