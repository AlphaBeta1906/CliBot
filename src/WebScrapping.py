from selenium import webdriver

#browser.get('http://seleniumhq.org/')

def split(keyword_split):
	keyword_split = "+".join(keyword_split)
	return keyword_split

def search(keyword):
	browser = webdriver.Chrome()
	browser.maximize_window()
	keyword = split(keyword)
	for i in range(1):
		 matched_elements = browser.get("https://www.google.com/search?q=" +keyword + "&start=" + str(i))
		
	print("\nsearch success\n")