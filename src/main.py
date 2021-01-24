import api
import voidCommand as void
import WebScrapping as web

#im = Image.open(requests.get("https://images.unsplash.com/photo-1485550409059-9afb054cada4?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MXx8cmFuZG9tfGVufDB8fDB8&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60",stream = True).raw)
#im.show()
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
	"search" : web.search
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
			NonVoidCommand[Input[0].lower()](Input[1:])
		elif Input[0] == "quit":
			break
		else:
			print("Unknown command")
if __name__ == '__main__':
	main()
#()
