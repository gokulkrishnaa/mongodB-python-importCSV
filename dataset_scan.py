# Run the import from Command line by specifying the path

# from terminal execute as "python dataset_scan.py -p <PATHNAME>"

import getopt
import os
import sys

#function to run through the files in folder
def run_through(path):
	k=path
	files = os.listdir(path)
	for file in files:
		if os.path.isfile(k+"/"+file):
			pass
			# mongoimport(file)
			# put the read CSV function and import to MongoDB function of "file_scan.py" file here.
		else:
			run_through(k+"/"+file)


def main(argv):
	try:
		opt,val= getopt.getopt(argv,'p:')
	except getopt.GetoptError:
		print "Unrecognised parameters"
		sys.exit(2)
	for a,s in opt:
		if a == '-p':
			path = s
	run_through(path)

if __name__ == '__main__':
  main(sys.argv[1:])