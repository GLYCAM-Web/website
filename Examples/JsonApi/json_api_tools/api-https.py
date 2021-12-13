import requests
import sys
import json
import traceback

# validate number of args
if len(sys.argv) != 3:
	print("invalid args")
	print("argv[1] must be a URL")
	print("argv[2] must be a path to .json file")
	exit(1)

# build URL string
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
	print("api-https.py: problem setting url")
	exit(1)

# open (and inadvertently validate) .json file and serialize to string
data = None
try:
	with open(sys.argv[2], 'r') as f:
		d = json.load(f)
		data = json.dumps(d)
except Exception as error:
	print("err -- api-https.py: could not open " + sys.argv[2])	
	print(traceback.format_exc())
	raise error

# get token, cookies; set headers
tokenurl = url + "/json/getToken"
try: 
	response = requests.get(tokenurl)	
except Exception as error:
	print("err -- api-https.py: could not request token from " + tokenurl)
	print(traceback.format_exc())	
	raise error

token = response.text
cookies = response.cookies
headers = {
	"X-CSRFToken": token,
	'Content-Type': 'application/json',
	}

# post .json request
apiurl = url + "/json/"
try:
	response = requests.post(apiurl, headers=headers, data=data, cookies=cookies)	
except Exception as error:
	print("err -- api-https.py: could not post .json to " + apiurl)
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
	print("err -- api-https.py: could not open " + sys.argv[2])	
	print(traceback.format_exc())
	raise error
