import subprocess
import sys
import os
import fileinput

def install_nix():
    pythonlocation = subprocess.check_output(["which", "python"], shell=False)
    if "python27" in pythonlocation:
        path = pythonlocation.replace("python27\n", "")
    elif "python" in pythonlocation: 
        path = pythonlocation.replace("python\n", "")
    pwd = subprocess.check_output("pwd", shell=False).replace("\n", "")
    installwd = "{}/lr/logroller/lr".format(pwd)
    installreq = "{}/lr/logroller/requirements.txt".format(pwd)
    sed = "s@\#\#SHEBANG\#\#@\#\!{}@g".format(pythonlocation.replace("\n", ""))
    subprocess.call(["sed", "-i", "-e" , sed, installwd], shell=False)

    remotepath = raw_input("Specify the absolute remote path that lr will search by default: (ex. /var/log/) ")
    if remotepath[-1:] != "/":
        print "Path must end with slash (ex. /var/log/)"
        remotepath = raw_input("Specify the absolute remote path that lr will search by default: (ex. /var/log/) ")
    else:
        sed = "s@\#\#REMOTEPATH\#\#@{}@g".format(remotepath.replace("\n", ""))
        subprocess.call(["sed", "-i", "-e", sed, installwd], shell=False)

    localpath = raw_input("Specify the absolute local path that lr will store the logs in: (ex. /home/username/) ")
    if localpath[-1:] != "/":
        print "Path must end with slash (ex. /home/username/)"
        remotepath = raw_input("Specify the absolute remote path that lr will search by default: (ex. /var/log/) ")
    else:
        sed = "s@\#\#LOCALPATH\#\#@{}@g".format(localpath.replace("\n", ""))
        subprocess.call(["sed", "-i", "-e", sed, installwd], shell=False)
    subprocess.call(["cp", installwd, path], shell=False)
    subprocess.call(["pip", "install", "-r", installreq], shell=False)
    print "Successfully installed lr"


platform = sys.platform.lower()
if "nt" in platform:
    print "Windows based system"
elif "cygwin" in platform:
    install_nix()
elif "linux" in platform: 
    install_nix()