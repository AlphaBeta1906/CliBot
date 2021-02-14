import socket
from datetime import date
import os
import WebScrapping
import File

# void command

"""
contains simple command to interact with computer
"""
hostname = socket.gethostname()


def Date():
    today = date.today()
    print("today date : " + str(today))


def name():
    print("Your pc name : " + hostname)


def ip():
    print("Your IP addres : " + socket.gethostbyname(hostname))


def clr():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def Help():
    WebScrapping.startBrowser(
        "https://github.com/AlphaBeta1906/CliBot/blob/master/README.md"
    )


def run(file):
    try:
        cmd = "python " + os.path.join(
            File.Path, file[0]
        )  # python command and python file will joined
        os.system(cmd)
    except KeyboardInterrupt:
        return


# ()
