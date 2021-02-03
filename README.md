[![CodeFactor](https://www.codefactor.io/repository/github/alphabeta1906/clibot/badge)](https://www.codefactor.io/repository/github/alphabeta1906/clibot)
# CliBot
Is this a cli?is this a bot?I don't know, this is just releasing boredom during the pandemic¯\_(ツ)_/

## About CliBot
well i even don't know what is this and why i create it, it just a program that have several simple command which can help your work or just playing around with command :D
# available commands(for now)
### Api
|command   | output  |
|---|---|
|  ufact | return random useless fact :p  |
|  bored | return a suggestion of activity |
<!---|  covid|  return the report of covid-19 data (disabled)|
|  jokes | return a random jokes (disabled)|
|  weather < city >  |  return a report of current weather in city (disabled)|-->


### web scrapping
|command | output  |
|---|---|
| search < keyword > | automatically open google chrome to show result|
| wikped < keyword >  | automatically open wikipedia search to show result|
| link < url/link > | find url e.g github.com,stackoverflow.com etc and not a keyword|
  
### math
to use these command you must type ```math``` followed by command below 
|command | output  |
|---|---|
| sum  | sum of all number |
| subs | subs of all number |
| mult | multipication of all number |
| div | division of all number |
| avg | avearage of all number |

after input the command above it must followed by series of number delimited by ```,```
example : ``` math sums 8,9,5 ``` 


### file handling
|command | output  |
|---|---|
| cfile < filename or path to the file > < content(optional) > |create file in current path example : `cfile hello.txt this is content`. Hello is file name, and the rest will be content(one line) |
| dfile < filename or path to the file > | delete file in current path |
| cdir < folder name > | create folder in current path |
| set < dir1 > < subDir1 > < subdir of subDir1 > | change the current path, you can manipulate your file/folder in current directory,you can use space or `/` as delimiter . example : `set desktop MyFolder` or `set/desktop/MyFolder` . unfortunately you can acces sub folder of current path you set,you must re-set again(arrow up in cmd) and add your sub folder of subfolder, it may be fixed in the future :grin: |

### other's
|command | output  |
|---|---|
|  date | return date now   |
|  name | return your machine name|
|  clr  | clear the terminal|
|  quit | quit program |
|  ip   | show your ip |

## how to contribute
requirement :
1. [git](https://git-scm.com/downloads) to clone this project
2. virtual evniroment, use ```pip install virtualenv``` if not installed in your machine
3. Chrome web driver, to run webscrapping.py
4. of course you need [python](https://www.python.org/downloads/) to compile the program, i use python 3.9 to write this program
5. code/text editor to write the code

How to compile:
```bash
> git clone https://github.com/AlphaBeta1906/CliBot.git #clone the project
> cd path/where/youClone/this #go to the dir where you clone this project
> venv/scripts/activate #activating virtual enviroment for windows
> venv/bin/activate #for activating virtual enviroment for linux(maybe?)
> pip install -r requirements.txt #to install the libraries
> python src/main.py #run the main scripts 
```

features of this app is still low and it will be great if you add some feature/command or improve this README(because i'm not good at expalain something)<br/>
*note : you can add api as long as they **NOT** required key*
  
## License
### [MIT](https://github.com/AlphaBeta1906/CliBot/blob/master/LICENSE)
