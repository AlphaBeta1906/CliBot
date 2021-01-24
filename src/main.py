
import api
import voidCommand as void
#import WebScrapping as web

#non void command
#well, it's just experimental
def Hello(name):
	print("Hello " + name)

voidCommand = {
	"date" : void.Date,
	"name" : void.name,
	"ip" : void.ip,
	"clr" : void.clr,
	#"jokes" : api.Jokes,
	#"covid" : api.covid,
	"ufact" : api.UselessFact
}
NonVoidCommand = {
	"hello" : Hello,
}
searchCommand = {
	#"search" : web.search,
	#"weather" : api.weather
}

def main():
	while True:
		Input = input("type your input ")
		Input = Input.split(' ')
		if Input[0].lower() in voidCommand:
			voidCommand[Input[0].lower()]()
			if len(Input) >= 2:
				print("anything that come after command will be ignored")
		elif Input[0].lower() in NonVoidCommand:
			NonVoidCommand[Input[0].lower()](Input[1])
			if len(Input) > 2:
				print("anything that come after the argument will be ignored")
		elif Input[0].lower() in searchCommand:
			searchCommand[Input[0].lower()](Input[1:])
		elif Input[0] == "quit":
			break
		else:
			print("Unknown command")

if __name__ == '__main__':
	main()
#()