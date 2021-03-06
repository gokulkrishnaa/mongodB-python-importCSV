# Import the CSV file specified under Path into MongoDB

import os, pprint, csv
from pymongo import MongoClient

client=MongoClient()
db=client['newest']

# Function to read a CSV file and import to MongoDB
def file_csv_read(file,name):
	with open(file,'rb') as csvfile:
		parse=csv.DictReader(csvfile, delimiter=',', quotechar='"', skipinitialspace=True)
		for data in parse:
			import_to_mongo(data,name)

def import_to_mongo(data,name):
	col=db[name]
	col.insert(data)


path="/Users/GK/Downloads/dataset/dataset/app_usage"
files = os.listdir(path)
i=1
#read files from a folder
for file in files:
	file_csv_read(path+"/"+file,file)
	break