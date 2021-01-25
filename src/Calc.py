import math

#()
"""
	print(argument[0])
	argument = argument[0].split()
	return argument[0]
"""
def Add(value):
	print(sum(value))

def subs(value):
	res = value[0]
	for i in range(0,len(value)):
		if i == 0:
			continue
		res -= value[i]
	print(res) 

def multi(value):
	res = value[0]
	for i in range(0,len(value)):
		if i == 0:
			continue
		res *= value[i]
	print(res)


def div(value):
	res = value[0]
	divZero = False
	for i in range(0,len(value)):
		if i == 0:
			continue
		try:
			res /= value[i] 
		except ZeroDivisionError:
			print("divide by zero exception")
			res = 0
			break
	print(res)

def avg(value):
	print(sum(value)/len(value))

calc = {
	"sum" : Add,
	"subs" : subs,
	"multi" : multi,
	"div" : div,
	"avg" : avg
}

def converter(argument):
	array = argument[1].split(',')
	arry = argument[1].replace(',','')
	cmd = argument[0]
	try:
		for i in range(0,len(array)):
			array[i] = float(array[i])
	except ValueError:
		print("Value error,there are letter in your number")
	else:
		calc[cmd](array)
