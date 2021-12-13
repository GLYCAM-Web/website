import requests
import sys
import json
import traceback

# validate number of args
if len(sys.argv) != 4:
	print("invalid args")
	print("argv[1] must be a URL")
	print("argv[2] must be a pUUID")
	print("argv[3] must be a file name")
	exit(1)

# validate and build URL string
url = None
if isinstance(sys.argv[1], str):
	# if dev environment, use http protocol
	if "glycam" not in sys.argv[1]:
		url = "http://" + sys.argv[1]
	# else live site, use https protocol
	else:
		url = "https://" + sys.argv[1]
	#print("target url is: " + str(url))
elif url == None:
	print("downloadDefaultStructure.py: problem setting url")
	exit(1)

# validate and set pUUID
pUUID = None
if isinstance(sys.argv[2], str):
	pUUID = sys.argv[2]
else:
	print("downloadDefaultStructure.py: problem setting pUUID")
	exit(1)

# validate and set file name
filename = None
if isinstance(sys.argv[3], str):
	filename = sys.argv[3]
else:
	print("downloadDefaultStructure.py: problem setting pUUID")
	exit(1)

pdburl = url + "/json/download/sequence/cb/" + pUUID + "/"
try: 	
	response = requests.get(pdburl)
except:
	print("err -- downloadDefaultStructure.py: could not download from " + pdburl)
	print(traceback.format_exc())	
	raise error

# save .pdb
pdb = response.text
print(pdb)
try:
	with open(filename, "w") as f:
		f.write(pdb)
except:
	print("err -- downloadDefaultStructure.py: problem saving .pdb")
	print(traceback.format_exc())
	raise error
