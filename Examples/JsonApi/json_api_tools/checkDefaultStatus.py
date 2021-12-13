import requests
import sys
import json
import traceback

# validate number of args
if len(sys.argv) != 3:
	print("invalid args")
	print("argv[1] must be a URL")
	print("argv[2] must be a pUUID")
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
	print("checkDefaultStatus.py: problem setting url")
	exit(1)

# validate and set pUUID
pUUID = None
if isinstance(sys.argv[2], str):
	pUUID = sys.argv[2]
else:
	print("checkDefaultStatus.py: problem setting pUUID")
	exit(1)

# poll
apiurl = url + "/json/project_status/sequence/" + pUUID + "/"
try:
	response = requests.get(apiurl)
except Exception as error:
	print("err -- checkDefaultStatus.py: problem with request to " + apiurl)
	print(traceback.format_exc())	
	raise error

print(response.text)

# save output
from datetime import datetime
now = datetime.now()
datestring = now.strftime("%Y.%m.%d.%H.%M.%S")
filename = sys.argv[2] + "." + datestring + ".Response" + ".json"
# filename = sys.argv[2] + ".Response" + ".json"
try: 
	# is a call to dumps() redundant because of the Content-Type header?
	jsonresponse = json.dumps(response.text)
	with open(filename, "w") as f:
		f.write(jsonresponse)
except Exception as error:	
	print("err -- checkDefaultStatus.py: could not open " + sys.argv[2])	
	print(traceback.format_exc())
	raise error