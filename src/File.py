import os
import getpass
import shutil
from colorama import Fore, init

init(convert=True)
# ()
Home = (
    "C:/Users/" + getpass.getuser() + "/"
)  # for now the default path is for windows only

"""
set dir : set <path to dir> you can use / or space to write it
			  you must set again if you want to change dir
			  example : set desktop/folder or set desktop folder
			  and if you wan to move to sub dir : set desktop/folder/subfolder or set desktop folder sub folder
create new file : cfile <path + filename and ext or just filename and ext>

delete file : cfile <path + filename and ext or just filename and ext>

create directory/folder : cdir <folderName> <file for the folder(optional)>
"""


def setPath(argument):
    global Path
    Path = Home
    if argument[0] == "home":
        Path = Home
    else:
        argument = "/".join(argument)
        if (
            os.path.exists(Home + argument)
            and os.path.isdir(Home + argument)
            and argument != Home
        ):
            Path = os.path.join(Home + argument)
        else:
            print(Fore.RED + "Error :" + Path + " not exist")
            Path = Home


# cfile <filename.format> |create one either empty file or one one line file
def cfile(argument):
    content = " ".join(argument[1:])
    path = os.path.join(Path, argument[0])
    try:
        if not os.path.exists(path):

            file = open(path, "w")
            file.write(content)
            file.close()
            print("file succesfully created at  : " + path)
        else:
            print("file or folder with same name already exist")
    except FileNotFoundError:
        print(Fore.RED + "Error : " + path + "not found")
    except OSError:
        print(Fore.RED + "Error  : failed create file at " + path)
    else:
        print(Fore.GREEN + "Succes : file succesfully created at " + path)


# example : dfile <filename> | delete only one file
def dfile(argument):
    argument = "/".join(argument)
    path = os.path.join(Path, argument)
    if os.path.exists(path) and os.path.isfile(path):
        os.remove(path)
        print("succesfully delete : " + argument)
    else:
        print(Fore.RED + "error " + argument + " maybe is not a file or not exist")


# example : cdir file.txt file2.txt.... | delimeted by space
def cdir(argument):
    files = argument[1:]
    path = os.path.join(Path, argument[0])
    try:
        os.mkdir(path)
        for i in range(len(files)):
            file = open(path + "/" + files[i], "w")
            file.close()
    except FileNotFoundError:
        print(Fore.RED + "Error : path not found")
    except FileExistsError:
        print(Fore.RED + "Error : dir already exist")
    except OSError:
        print(Fore.RED + "Error : failed creating folder")
    else:
        print(Fore.GREEN + " folder created at " + path)


# example ddir <folderName> | delete one folder
def ddir(argument):
    argument = "/".join(argument)
    path = os.path.join(Path, argument)
    try:
        shutil.rmtree(path)
    except FileNotFoundError:
        print(Fore.RED + "Error : " + argument + " not exist")
    except OSError:
        print(Fore.RED + "Error : failed when delete dir")
    else:
        print(Fore.GREEN + "Success : folder deleted at " + path)


def ShowList(path):
    try:
        print(path)
        cmd = "dir " + os.path.join(Path, "\\".join(path))
        cmd = cmd.replace("/", "\\")
        os.system(cmd)
    except IndexError:
        cmd = Path.replace("/", "\\")
        if Path == Home:
            cmd = list(cmd[:-1])
            cmd = "".join(cmd)
            os.system("dir " + cmd)
        else:
            os.system("dir " + cmd)


def multi(List):
    for fileOrDir in List:
        try:
            if fileOrDir[-1] == "\\" or fileOrDir[-1] == "/":
                os.mkdir(os.path.join(Path, fileOrDir))
            else:
                file = os.path.join(Path, fileOrDir)
                file = open(file, "w")
                file.close()
        except OSError:
            print("Error : failed create list of files at " + Path)
        else:
            print(Fore.GREEN + "Success : list of  files created at " + Path)


setPath(Home)  # initialize deafult path
# ()wtf sublime text can't use : ()
