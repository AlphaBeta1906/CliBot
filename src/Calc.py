import math
from colorama import Fore,Style,init 
init(convert=True)
#()
"""
	print(argument[0])
	argument = argument[0].split()
	return argument[0]
"""

def simple(command,value):
	res = value[0]
	for i in range (0,len(value)):
		if i == 0:
			continue
		if command == "sum":
			res += value[i]
		elif command == "subs":
			res -= value[i]
		elif command == "multi":
			res *= value[i]
		elif command == "div":
			try:
				res /= value[i]
			except ZeroDivisionError:
				print(Fore.RED + "divison by zero error!")
				res = 0
		else:
			print(Fore.RED + "unknown command :" + command)
			res = None
			break
	print("result : " + str(res) + "\n")

def avg(value):
	print("average result : " + str((round(sum(value)/len(value),2))) + "\n" )

calc = {
	"avg" : avg
}

def converter(argument):
	try:
		array = argument[1].split(',')
		#array = argument[1].replace(',','')
		cmd = argument[0]
		try:
			for i in range(0,len(array)):
				array[i] = float(array[i])
		except ValueError:
			print(Fore.RED + "Value error : your value is not number!")
		else:
			try:
				calc[cmd](array)
			except KeyError:
				simple(cmd,array)
	except IndexError:
		print(Fore.RED + "IndexError: your number/value is empty or not a number!")