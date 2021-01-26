import api
import voidCommand as void
import WebScrapping as web
import Calc
from colorama import Fore,Style,init
init(convert=True)

#()

#non void command
#well, it's just experimental
def Hello(name):
	print("Hello " + name)

voidCommand = {
	"date" : void.Date,
	"name" : void.name,
	"ip" : void.ip,
	"clr" : void.clr,
	"ufact" : api.UselessFact,
	"bored" : api.bored
}

NonVoidCommand = {
	"hello" : Hello,
	"search" : web.search,
	"wikped": web.wikipedia,
	"link" : web.link,
	"math" : Calc.converter
}

void.clr()
print(Fore.GREEN + "CliBot [ver: dev-Version]")
print(Fore.YELLOW + Style.DIM + "(c) 2021")
def main():
	while True:
		print(Fore.WHITE)
		Input = input("type your input ")
		Input =  Input.lstrip()
		Input = Input.split(' ')
		if Input[0].lower() in voidCommand:
			voidCommand[Input[0].lower()]()
			if len(Input) >= 2:
				print("anything that come after command will be ignored")

		elif Input[0].lower() in NonVoidCommand:
			NonVoidCommand[Input[0].lower()](Input[1:])

		elif Input[0] == "quit":
			break

		else:
			print(Fore.RED + "Unknown command: " + Input[0] )

if __name__ == '__main__':
	main()
#()
