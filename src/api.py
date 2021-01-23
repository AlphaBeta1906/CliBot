import ApiModule as apm
from datetime import date
import config


"""	

#you must have my permision to add api('s) that require key
def covid():
	try:
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
	except:
		print("connection error")

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
	except:
		print("connection error")
"""
def weather(location):
	location = " ".join(location)
	complete_url = config.weather_key  + "&q=" + location
	myDict = apm.Handle(complete_url)
	weather = myDict['weather'][0]
	temperature = myDict['main']
	
	print("")
	print("city name : " + location)
	print("weather : " + weather['main'])
	print("description : " + weather['description'] )
	print("temperature : " + str( round(temperature['temp'] - 273,0)) + "°C" )
	print("humidity : " + str(temperature['humidity'] )+"%")
	print("country : " + myDict['sys']['country'] + "\n")

def UselessFact():
	url = "https://uselessfacts.jsph.pl/random.json?language=en"
	myDict = apm.Handle(url)
	print("here a random useless fact : " + myDict['text'] + "\n")