import ApiModule as apm
from datetime import date

def UselessFact():
	url = "https://uselessfacts.jsph.pl/random.json?language=en"
	myDict = apm.Handle(url)
	print("here a random useless fact : " + myDict['text'] + "\n")