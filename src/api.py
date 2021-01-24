import requests
import json

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

def UselessFact():
	url = "https://uselessfacts.jsph.pl/random.json?language=en"
	myDict = Handle(url)
	print("here a random useless fact : " + myDict['text'] + "\n")

def bored():
	url = "https://www.boredapi.com/api/activity"
	myDict = Handle(url)
	print("are you bored? try this activity : " + myDict['activity'])