import requests
import json
from requests.auth import HTTPBasicAuth

PROJECT_ID = "3a14d63b6f774200aeea94ca05b76782"
PROJECT_SECRET = "odkJBNEuksxsSFKlGhIJipVkmYQYoB3G5jqHGXQB+97+wpxGpnHADQ"

def pin_to_ipfs(data):
	assert isinstance(data,dict), f"Error pin_to_ipfs expects a dictionary"
	#YOUR CODE HERE
	url = "https://ipfs.infura.io:5001/api/v0/add"
	json_data = json.dumps(data)
	files = {'file': ('data.json', json_data, 'application/json')}
	response = requests.post(url, files=files, auth=HTTPBasicAuth(PROJECT_ID, PROJECT_SECRET))
	if response.status_code == 200:
		cid = response.json().get("Hash")  # Extract CID from response
		return cid
	else:
		raise Exception(f"IPFS upload failed: {response.text}")



def get_from_ipfs(cid,content_type="json"):
	assert isinstance(cid,str), f"get_from_ipfs accepts a cid in the form of a string"
	#YOUR CODE HERE
	url = "https://ipfs.infura.io:5001/api/v0/cat"
	params = {"arg": cid}
	response = requests.post(url, params=params, auth=HTTPBasicAuth(PROJECT_ID, PROJECT_SECRET))
	if response.status_code == 200:
		try:
			data = json.loads(response.text)  # Convert JSON string back to Python dictionary
			assert isinstance(data, dict), "Error: get_from_ipfs should return a dictionary"
			return data
		except json.JSONDecodeError:
			raise Exception("Error: The retrieved content is not valid JSON.")
	else:
		raise Exception(f"Error fetching data from IPFS: {response.text}")

