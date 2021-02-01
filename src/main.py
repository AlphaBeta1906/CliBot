import api
import SimpleCommand as simple
import WebScrapping as web
import Calc
import File
from colorama import Fore,Style,init
import os
init(convert=True)

#()


#well, it's just experimental
def Hello(name):
	print("Hello " + name)

#just command, argument will be ignored
simpleCommand = {
	"date":simple.Date,
	"name":simple.name,
	"ip":simple.ip,
	"clr":simple.clr,
	"ufact":api.UselessFact,
	"bored":api.bored,
	}

#NonVoidCommand aka command that need argument
NonVoidCommand = {
	"hello":Hello,
	"search":web.search,
	"wikped":web.wikipedia,
	"link":web.link,
	"math":Calc.converter,
	"cfile":File.cfile,
	"set" : File.setPath,
	"dfile": File.dfile,
	"cdir":File.cdir,
	"ddir":File.ddir
	}

simple.clr()
print(Fore.GREEN + "CliBot [ver: dev-Version]")
print(Fore.YELLOW + Style.DIM + "(c) 2021")
def main():
	while True:
		try:
			print(Fore.WHITE)
			print("current path : " + File.Path)
			Input = input("type your input ")
			Input =  Input.lstrip()
			Input = Input.split(' ')
			if Input[0].lower() in simpleCommand:
				simpleCommand[Input[0].lower()]()
				if len(Input) >= 2:
					print("anything that come after command will be ignored")

			elif Input[0].lower() in NonVoidCommand:
				NonVoidCommand[Input[0].lower()](Input[1:])

			elif Input[0] == "quit":
				break
				
			else:
				print(Fore.RED + "Unknown command: " + Input[0] )
		except KeyboardInterrupt:
			break
		except EOFError:
			break;

if __name__ == '__main__':
	main()
#()
