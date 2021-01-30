import os
import getpass
from colorama import Fore,init,Style
init(convert=True)
#()
Home = "C:/Users/" + getpass.getuser() + "/"

"""
set new dir : set <path to dir> you can use / or space to write it
			  you must set again if you want to change dir
			  example : set desktop/folder or set desktop folder
			  and if you wan to move to sub dir : set desktop/folder/subfolder or set desktop folder sub folder
create new file : cfile <path + filename and ext or just filename and ext>

delete file : cfile <path + filename and ext or just filename and ext>

create directory/folder : cdir <folderName> <file for the folder(optional)>
"""
def setPath(argument):
	argument = "/".join(argument)
	global Path
	if os.path.exists(Home + argument) and os.path.isdir(Home + argument) and argument != Home:
		Path = os.path.join(Home + argument)
		print("set current dir to : " + Path)
		print("you can manipulate file in this dir")
	else:
		print("path not exist")
		Path = Home

def cfile(argument):
	content = " ".join(argument[1:])
	path = os.path.join(Path,argument[0])
	try:
		if not os.path.exists(path):
			file = open(path,"w")
			file.write(content)
			file.close()
			print("file succesfully created at  : " + path)
		else:
			print("file already exists")
	except FileNotFoundError:
		print(Fore.RED + "error : " + path + "not found")

def dfile(argument):
	argument = "/".join(argument)
	path = os.path.join(Path,argument)
	if os.path.exists(path) and os.path.isfile(path):
		os.remove(path)
		print("succesfully delete : " + argument)
	else:
		print(Fore.RED + "error " + argument + " maybe is not a file or not exist")

def cdir(argument):
	files = argument[1:]
	path = os.path.join(Path,argument[0])
	try:
		os.mkdir(path)
		for i in range(0,len(files)):
			file = open(path+"/"+files[i],"w")
			file.write("")
			file.close()
	except FileNotFoundError:
		print("invalid command")
	except FileExistsError:
		print("dir already exist")
	else: 
		print("folder created at " + path)


setPath(Home)#initialize deafult path

#()wtf sublime text can't use : ()