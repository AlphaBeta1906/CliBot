import math

#()
"""
	print(argument[0])
	argument = argument[0].split()
	return argument[0]
"""

def simple(command,value):
	Simple = True
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
				print( "divison by zero error")
		else:
			print("unknown command")
			res = ""
			break
	print("result : " + str(res) + "\n")

def avg(value):
	print("average result : " + str((round(sum(value)/len(value),2))) + "\n" )

calc = {
	"avg" : avg
}

def converter(argument):
	array = argument[1].split(',')
	#array = argument[1].replace(',','')
	cmd = argument[0]
	try:
		for i in range(0,len(array)):
			array[i] = float(array[i])
	except ValueError:
		print("Value error,there are letter in your number")
	else:
		try:
			calc[cmd](array)
		except KeyError:
			simple(cmd,array)
