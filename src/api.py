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
	except:
		return NotFound

def UselessFact():
	try:
		url = "https://uselessfacts.jsph.pl/random.json?language=en"
		myDict = Handle(url)
		print("here a random useless fact : " + myDict['text'] + "\n")
	except TypeError:
		print("error")


def bored():
	try:
		url = "https://www.boredapi.com/api/activity"
		myDict = Handle(url)
		print("are you bored? try this activity : \n" + "activity name : "+ myDict['activity'])
		print("type : " + myDict['type'])
		print("number of partcipant : " + str(myDict['participants']))
		print("price : " + str(myDict['price']))
		link = myDict['link'] if myDict['link'] != "" else "none"
		print("link : " + link + "\n")
	except TypeError:
		print("error")