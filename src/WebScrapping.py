
from selenium import webdriver

#browser.get('http://seleniumhq.org/')

def split(keyword_split):
	keyword_split = "+".join(keyword_split)
	return keyword_split

def search(keyword):
	browser = webdriver.Chrome()
	browser.maximize_window()
	keyword = split(keyword)
	browser.get("https://www.google.com/search?q=" +keyword + "&start=" + str(1))