from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import time
from colorama import init, Fore

init(convert=True)

# browser.get('http://seleniumhq.org/')()


def startBrowser(url):
    try:
        print("please wait, it may take some time")
        browser = webdriver.Chrome(r".\src\driver\chromedriver.exe")
        browser.maximize_window()
        browser.get(url)
    except WebDriverException:
        time.sleep(3)
        print(Fore.RED + "connection error!!! ")
        try:
            browser.quit()
        except UnboundLocalError:  # throw when user suddenly close window or closed for no
            print(Fore.RED + "window closed sudennly")


def search(keyword):
    keyword = "+".join(keyword)
    url = "https://www.google.com/search?q=" + keyword + "&start=" + str(1)
    startBrowser(url)
    print("\n")


def wikipedia(keyword):
    keyword = "+".join(keyword)
    url = (
        "https://en.wikipedia.org/w/index.php?search="
        + keyword
        + "&title=Special:Search&profile=advanced&fulltext=1&advancedSearch-current=%7B%7D&ns0=1"
    )
    startBrowser(url)


def link(Link):  # must link/url not keyword
    Link = "".join(Link)
    url = "http://" + Link + "/"
    startBrowser(url)
