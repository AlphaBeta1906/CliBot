import api
import SimpleCommand as simple
import WebScrapping as web
import Calc
from colorama import Fore,Style,init
init(convert=True)

#()

#non simple command
#well, it's just experimental
def Hello(name):
	print("Hello " + name)

simpleCommand = {
	"date" : simple.Date,
	"name" : simple.name,
	"ip" : simple.ip,
	"clr" : simple.clr,
	"ufact" : api.UselessFact,
	"bored" : api.bored
}

NonsimpleCommand = {
	"hello" : Hello,
	"search" : web.search,
	"wikped": web.wikipedia,
	"link" : web.link,
	"math" : Calc.converter
}

simple.clr()
print(Fore.GREEN + "CliBot [ver: dev-Version]")
print(Fore.YELLOW + Style.DIM + "(c) 2021")
def main():
	while True:
		print(Fore.WHITE)
		Input = input("type your input ")
		Input =  Input.lstrip()
		Input = Input.split(' ')
		if Input[0].lower() in simpleCommand:
			simpleCommand[Input[0].lower()]()
			if len(Input) >= 2:
				print("anything that come after command will be ignored")

		elif Input[0].lower() in NonsimpleCommand:
			NonsimpleCommand[Input[0].lower()](Input[1:])

		elif Input[0] == "quit":
			break

		else:
			print(Fore.RED + "Unknown command: " + Input[0] )

if __name__ == '__main__':
	main()
#()
