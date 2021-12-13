import requests
import sys
import json
import traceback

# validate number of args
if len(sys.argv) != 4:
	print("invalid args")
	print("argv[1] must be a URL")
	print("argv[2] must be a pUUID")
	print("argv[3] must be a conformer ID")
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
	print("checkConformerStatus.py: problem setting url")
	exit(1)

# validate and set pUUID
pUUID = None
if isinstance(sys.argv[2], str):
	pUUID = sys.argv[2]
else:
	print("checkConformerStatus.py: problem setting pUUID")
	exit(1)

# validate and set conformer ID
conformerID = None
if isinstance(sys.argv[3], str):
	conformerID = sys.argv[3]
else:
	print("checkConformerStatus.py: problem setting pUUID")
	exit(1)

# poll
apiurl = url + "/json/build_status/" + pUUID + "/" + conformerID + "/"
try:
	# are headers and cookies needed in this context?	
	response = requests.get(apiurl)
except Exception as error:
	print("err -- checkConformerStatus.py: problem with request to " + apiurl)
	print(traceback.format_exc())	
	raise error

print(response.text)

# save output
from datetime import datetime
now = datetime.now()
datestring = now.strftime("%Y.%m.%d.%H.%M.%S")
filename = sys.argv[2] + "." + sys.argv[3] + "." + datestring + ".Response" + ".json"
# filename = sys.argv[2] + ".Response" + ".json"
try:	
	jsonresponse = json.dumps(response.text)
	with open(filename, "w") as f:
		f.write(jsonresponse)
except Exception as error:	
	print("err -- checkConformerStatus.py: could not open " + sys.argv[2])	
	print(traceback.format_exc())
	raise error