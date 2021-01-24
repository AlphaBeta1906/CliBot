import socket
from datetime import date
import os

#void command
hostname = socket.gethostname()
def Date():
	today = date.today()
	print("today date : " + str(today))
def name():
	print("Your pc name : "  + hostname)
def ip():
	print("Your local IP addres : " + socket.gethostbyname(hostname))
def clr(): 
	if os.name =='nt':
		os.system('cls')
	else:
		os.system('clear')   
#()