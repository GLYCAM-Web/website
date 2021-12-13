import requests
#from functions import buildmarcojson

response = requests.get('https://glycam.org/json/getToken/')
token = response.text
cookies = response.cookies
headers = {
"X-CSRFToken": token,
'Content-Type': 'application/json',
}

# post requires a JSON string
marco = { "entity" : { "type": "Delegator" } }
import json
data = json.dumps(marco)

response = requests.post('https://glycam.org/json/', headers=headers, data=data, cookies=cookies)
print(response.text)
