import requests
import json
from requests.auth import HTTPBasicAuth

PROJECT_ID = "9d9fdc2c7c504c7fb3fae437588bc99e"
PROJECT_SECRET = "LmpsrZtmimEnzlhS0U9HTWOUnTAUwpKkzoUBgnBkeo70zEYxmcBwVg"

def pin_to_ipfs(data):
	assert isinstance(data,dict), f"Error pin_to_ipfs expects a dictionary"
	#YOUR CODE HERE
	url = "https://ipfs.infura.io:5001/api/v0/add"
	json_data = json.dumps(data)
	files = {'file': ('data.json', json_data, 'application/json')}
	response = requests.post(url, files=files, auth=HTTPBasicAuth(PROJECT_ID, PROJECT_SECRET))

	return cid

def get_from_ipfs(cid,content_type="json"):
	assert isinstance(cid,str), f"get_from_ipfs accepts a cid in the form of a string"
	#YOUR CODE HERE
	
	assert isinstance(data,dict), f"get_from_ipfs should return a dict"
	return data
