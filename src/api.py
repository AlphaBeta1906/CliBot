import requests
from colorama import Fore,init
init(convert=True)

def Handle(url):
	try:
		response = requests.get(url, timeout = 10)
		result = response.json()
		if response.status_code == 200:
			return result
		elif response.status_code == 404:
			return "not found"
		elif response.status_code == 500:
			return "server error"
		else:
			return "something went wrong"
	except requests.exceptions.Timeout:
		return "connection timeout"
	except requests.exceptions.ConnectionError:
		return "connection error"
	except requests.exceptions.TooManyRedirects:
		return "to many redirects"

def UselessFact():
	try:
		url = "https://uselessfacts.jsph.pl/random.json?language=en"
		myDict = Handle(url)
		print("here a random useless fact : " + myDict['text'] + "\n")
	except TypeError:
		print(Fore.RED + myDict)

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
		print(Fore.RED + myDict)