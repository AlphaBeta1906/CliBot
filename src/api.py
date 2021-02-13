import requests
from colorama import Fore, init
import config

init(convert=True)

"""
this module contains some function that will display api to console
pay attention to api with keys don't forget to commented they out
because they need config module and that's module only own by me
"""


def Handle(url):
    try:
        response = requests.get(url, timeout=10)
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


# api with keys
def Jokes():
    try:
        url = "https://joke3.p.rapidapi.com/v1/joke"
        querystring = {"nsfw": "true"}

        headers = {
            "x-rapidapi-key": config.jokes_key,
            "x-rapidapi-host": "joke3.p.rapidapi.com",
        }

        response = requests.request("GET", url, headers=headers, params=querystring,timeout=10)

        if response.status_code:
            myDict = response.json()
            print(myDict["content"])
            print(" ")
        else:
            print("something went wrong")
            print(response.status_code)
    except requests.exceptions.ConnectionError:
        print(Fore.RED + "connection error")
    except requests.exceptions.Timeout:
        print(Fore.RED + "connection timeout")

# api with keys
def weather(location):
    try:
        location = " ".join(location)
        complete_url = config.weather_key + "&q=" + location
        myDict = Handle(complete_url)
        weather = myDict["weather"][0]
        temperature = myDict["main"]
    except TypeError:
        print(Fore.RED + myDict)
    else:
        print("")
        print("city name : " + location.lstrip())
        print("weather : " + weather["main"])
        print("description : " + weather["description"])
        print("temperature : " + str(round(temperature["temp"] - 273, 0)) + "°C")
        print("humidity : " + str(temperature["humidity"]) + "%")
        print("country : " + myDict["sys"]["country"] + "\n")


def UselessFact():
    try:
        url = "https://uselessfacts.jsph.pl/random.json?language=en"
        myDict = Handle(url)
    except TypeError:
        print(Fore.RED + myDict)
    else:
        print("here a random useless fact : " + myDict["text"] + "\n")


def bored():
    try:
        url = "https://www.boredapi.com/api/activity"
        myDict = Handle(url)
        print(
            "are you bored? try this activity : \n"
            + "activity name : "
            + myDict["activity"]
        )
        print("type : " + myDict["type"])
        print("number of partcipant : " + str(myDict["participants"]))
        print("price : " + str(myDict["price"]))
        link = myDict["link"] if myDict["link"] != "" else "none"
        print("link : " + link + "\n")
    except TypeError:
        print(Fore.RED + myDict)


def NumTrivia(value):
    try:
        query = value[0] if len(value) >= 1 and value[0].isdigit() else "random"
        url = "http://numbersapi.com/" + query + "/trivia"
        response = requests.get(url, timeout=10)
        print(response.text)
    except requests.exceptions.Timeout:
        print(Fore.RED + "timeout error")
    except requests.exceptions.ConnectionError:
        print(Fore.RED + "Connection error")
    except IndexError:
        url = "http://numbersapi.com/" + "random" + "/trivia"
        response = requests.get(url, timeout=10)
        print(response.text)
