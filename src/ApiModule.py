import requests
import json
#()
NotFound = "not found"
def Handle(url):
	try:
		response = requests.get(url)
		result = response.json()
		if response.status_code == 200:
			return result
		elif response.status_code == 404:
			return "not found"
		else:
			return NotFound
	except Exc:
		return NotFound
#def WithKey(url,key,query):