import requests
import json
from datetime import date
import config

	
def covid():
	url = "https://covid-19-data.p.rapidapi.com/totals"

	headers = {
    	'x-rapidapi-key': config.covid_key,
    	'x-rapidapi-host': "covid-19-data.p.rapidapi.com"
   	}

	response = requests.request("GET", url, headers=headers)
	if response.status_code:
		myDict = response.json()
		data = myDict[0]
		print("\nCovid 19 lastest data," + str(date.today())) 
		print("confirmed : " + str(data['confirmed']))
		print("Deaths : " + str(data['deaths']))
		print("Recovered : " + str(data['recovered']))
		print("Last updated : " + data['lastUpdate'] + "\n")

	else:
		print("something went wrong")
		print(response.status_code)
		
def Jokes():
	try:
		url = "https://joke3.p.rapidapi.com/v1/joke"
		querystring = {"nsfw":"true"}

		headers = {
    		'x-rapidapi-key': config.jokes_key,
    		'x-rapidapi-host': "joke3.p.rapidapi.com"
    	}

		response = requests.request("GET", url, headers=headers, params=querystring)

		if response.status_code:
			myDict = response.json()
			print(myDict['content'])
			print(" ")
		else:
			print("something went wrong")
			print(response.status_code)
	except Exception as e:
		print("something went wrong")

def UselessFact():
	url = "https://uselessfacts.jsph.pl/random.json?language=en"
	response = requests.get(url)
	myDict = response.json()
	if response.status_code == 200:
		print("\n")
		print("here a random useless fact : " + myDict['text']+"\n")
	else: 
		print("error")

def weather(location):
	#try:
	complete_url = config.weather_key  + "&q=" + location
	response = requests.get(complete_url)

	myDict = response.json()
	if response.status_code == 200:
		weather = myDict['weather'][0]
		temperature = myDict['main']
		print("")
		print("city name : " + location)
		print("weather : " + weather['main'])
		print("description : " + weather['description'] )
		print("temperature : " + str( round(temperature['temp'] - 273,0)) + "°C" )
		print("humidity : " + str(temperature['humidity']) + "%\n")
	else:
		print("city not found\n")
