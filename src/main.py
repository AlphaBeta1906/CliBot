import api
import SystemCommand as simple
import WebScrapping as web
import Calc
import File
from colorama import Fore, Style, init

init(convert=True)

# ()
# Version 0.0.1


# just command, argument will be ignored
simpleCommand = {
    "date": simple.Date,
    "name": simple.name,
    "ip": simple.ip,
    "clr": simple.clr,
    "ufact": api.UselessFact,
    "bored": api.bored,
    "help": simple.Help,
    "jokes": api.Jokes,
}

# NonVoidCommand aka command that need argument
NonVoidCommand = {
    "search": web.search,
    "wikped": web.wikipedia,
    "link": web.link,
    "math": Calc.converter,
    "cfile": File.cfile,
    "set": File.setPath,
    "dfile": File.dfile,
    "cdir": File.cdir,
    "ddir": File.ddir,
    "weather": api.weather,
    "numtrivia": api.NumTrivia,
    "run":simple.run,
    "locate":api.locate
}

simple.clr()
print(Fore.GREEN + "CliBot [ver: v0.0.1]")
print(Fore.YELLOW + Style.DIM + "Copyright (c) 2021 AlphaBeta MIT License")


def main():
    while True:
        try:
            print(Fore.WHITE)
            print("current path : " + File.Path)
            Input = input("type your input ")
            Input = Input.lstrip()
            Input = Input.split(" ")
            if Input[0].lower() in simpleCommand:
                simpleCommand[Input[0].lower()]()
                if len(Input) >= 2:
                    print("anything that come after command will be ignored")

            elif Input[0].lower() in NonVoidCommand:
                NonVoidCommand[Input[0].lower()](Input[1:])

            elif Input[0] == "quit":
                break

            else:
                print(Fore.RED + "Unknown command: " + Input[0])
        except KeyboardInterrupt:
            break
        except EOFError:
            break


if __name__ == "__main__":
    main()
# ()
