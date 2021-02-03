import math
from colorama import Fore, Style, init

init(convert=True)
# ()
"""
this module contains math operation and formula
for now is only two command : simple command(sum,subs,multi,div) and average command(avg)
"""


def simple(command, value):
    res = value[0]
    for i in range(0, len(value)):
        # check the command
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
                res = None
        else:
            print(Fore.RED + "unknown command :" + command)
            res = None
            break
    print(
        "result : " + str(res) + "\n"
    )  # will print None if ZeroDivisionError exception was thrown


# calld when avg command was called from dict
def avg(value):
    print("average result : " + str((round(sum(value) / len(value), 2))) + "\n")


# calc command dict
calc = {
    "avg": avg,
}
"""
all input from 'math' command in main.py will go trough this function
they will be checked,converted and splited which will be used in math operation
"""


def converter(argument):
    try:
        array = argument[1].split(",")
        # array = argument[1].replace(',','')
        cmd = argument[0]
        try:
            for i in range(0, len(array)):
                array[i] = float(array[i])
        except ValueError:  # execute if ValyError was thrown(not number,non exist)
            print(Fore.RED + "Value error : your value is not number!")
        else:
            try:  # check input in command dict
                calc[cmd](array)
            except KeyError:  # execute if KeyError was thrown
                simple(cmd, array)
    except IndexError:
        print(Fore.RED + "IndexError: your number/value is empty or not a number!")
