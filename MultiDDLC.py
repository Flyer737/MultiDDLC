#MultiDDLC the Doki Doki Literature Club instancer,
#for those who enjoy the game with mods.

import os
import time
import random
import zipfile

global platform
running=True

platform = "Linux".title() #Options: Linux or Windows

DDLC_MASTER="DDLC_"+platform+"-core.zip"

cs = "MultiDDLC>"
BLUE="\u001b[34m"
RED="\u001b[31m"
GREEN="\u001b[32m"
YELLOW="\u001b[33m"
MAGENTA="\u001b[35m"
CYAN="\u001b[36m"
NoN="\u001b[0m"

#Logic
def cls():
	if platform=="Linux":
		os.system("clear")
	if platform=="Windows":
		os.system("cls")

def delete(file):
	if platform=="Linux":
		os.system("rm -rf "+file)
	if platform=="Windows":
		os.system("DEL /F /A "+file)

def help():
	cls()
	print("\u001b[4mCommands\u001b[0m")
	print("new [instance name]")
	print("Create a new instance (Name must not contain spaces!\n")
#	print("mod [instance name]")
#	print("Does it's best to autoinstall a mod from a zip file.\n")
	print("play [instance name]")
	print("Play an instanced copy of DDLC.\n")
	print("del [instance name]")
	print("Removes and instance and it's files.\n")

def randomColor():
	randInt = random.randint(0,6)
	if randInt==0:
		return "BLUE"
	elif randInt==1:
		return "RED"
	elif randInt==2:
		return "GREEN"
	elif randInt==3:
		return "YELLOW"
	elif randInt==4:
		return "MAGENTA"
	elif randInt==5:
		return "CYAN"
	elif randInt==6:
		return "NoN"

def newInstance(instanceName):
	print("Creating instance "+instanceName+"!")
	print("Extracting from "+DDLC_MASTER+"...")
	file = open("Instance_data.config","r")
	stuff = file.readlines()
	file.close()

	file = zipfile.ZipFile(DDLC_MASTER,"r")
	file.extractall(instanceName)
	file.close()

	if stuff[0]=="No instances detected!\n":
		delete("Instance_data.config")
		file = open("Instance_data.config","w")
		file.write(instanceName+"\n"+randomColor()+"\n")
		file.close()
	else:
		file = open("Instance_data.config","a")
		file.write(instanceName+"\n"+randomColor()+"\n")
		file.close()
	cls()

def removeInstance(removing):
	file = open("Instance_data.config","r")
	instances = file.readlines()
	instances2 = []
	instanceFinal = []
	for i in range(len(instances)):
		instances2.append(instances[i].replace("\n",""))
	file.close()
	delete("Instance_data.config")

	delete(removing)
	file = open("Instance_data.config","w")
	for i in range(len(instances2)):
		if instances2[i] != removing:
			instanceFinal.append(instances2[i]+"\n")
		else:
			toRemove=i
	instanceFinal.remove(instanceFinal[toRemove])
	for i in range(len(instanceFinal)):
		file.write(instanceFinal[i])
	if instanceFinal==[]:
		file.close()
		delete("Instnaces_data.config")
		file = open("Instance_data.config","w")
		file.write("No instances detected!\nYELLOW")
		file.close()

	file.close()
	cls()

def play(x):
	os.chdir(x)
	if platform=="Linux":
		os.system("wine DDLC.exe")
	if platform=="Windows":
		os.system("start DDLC.exe")
	os.chdir("..")

#def mod(inst):
#	os.chdir("Mod zips")


#Start up
cls()
try:
	file = open("Instance_data.config","r")
	file.close()
except FileNotFoundError:
	file = open("Instance_data.config","w")
	file.write("No instances detected!\nYELLOW")
	file.close()

try:
	os.mkdir("Mod zips")
except FileExistsError:
	pass

#Menu
instance_conf = open("Instance_data.config","r")
instances = instance_conf.readlines()
instance_conf.close()
print("Type (h)elp for help.")
while running:
	print("\u001b[4m\u001b[45mMultiDDLC\u001b[0m")
	print("\nInstances:")
	if "No Instances detected!" in instances:
		print("No instances detected!")
	else:
		for i in range(int(len(instances)/2)):
			x = eval(instances[(i*2)+1])
			print(x+instances[i*2].replace("\n","") + NoN)

	x=input("\n"+cs)
	if x=="e".lower() or x.lower()=="exit":
		exit()
	elif x.lower()=="h" or x.lower()=="help":
		help()
	elif 'new' in x.lower():
		name = x.replace("new ","").strip()
		newInstance(name)
		instance_conf = open("Instance_data.config","r")
		instances = instance_conf.readlines()
		instance_conf.close()
	elif "del" in x.lower():
		name = x.replace('del ','').strip()
		removeInstance(name)
		instance_conf = open("Instance_data.config","r")
		instances = instance_conf.readlines()
		instance_conf.close()
	elif "play" in x.lower():
		name = x.replace('play ','').strip()
		play(name)
	elif "mod" in x.lower():
		name = x.replace('mod ','').strip()
		mod(name)
	else:
		cls()




