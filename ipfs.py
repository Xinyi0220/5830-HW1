import requests
import json


PROJECT_ID = "c2bc880c7c59aad11545"
PROJECT_SECRET = "affd7b5a5d392f706f1016154d157b0171e97e781bbc7edefe588e12e7f9afbf"

def pin_to_ipfs(data):
	assert isinstance(data,dict), f"Error pin_to_ipfs expects a dictionary"
	#YOUR CODE HERE
	url = "https://api.pinata.cloud/pinning/pinJSONToIPFS"
	headers = {
		"pinata_api_key": PROJECT_ID,
		"pinata_secret_api_key": PROJECT_SECRET,
		"Content-Type": "application/json"
	}
	response = requests.post(url, headers=headers, json={"pinataContent": data})
	if response.status_code == 200:
		cid = response.json().get("IpfsHash")  # Extract CID from response
		return cid
	else:
		raise Exception(f"IPFS upload failed: {response.text}")


def get_from_ipfs(cid,content_type="json"):
	assert isinstance(cid,str), f"get_from_ipfs accepts a cid in the form of a string"
	#YOUR CODE HERE
	url = f"https://gateway.pinata.cloud/ipfs/{cid}"
	response = requests.get(url)
	if response.status_code == 200:
		try:
			data = json.loads(response.text)  # Convert JSON string back to Python dictionary
			assert isinstance(data, dict), "Error: get_from_ipfs should return a dictionary"
			return data
		except json.JSONDecodeError:
			raise Exception("Error: The retrieved content is not valid JSON.")
	else:
		raise Exception(f"Error fetching data from IPFS: {response.text}")

