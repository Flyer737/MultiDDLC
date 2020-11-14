import zipfile
import os

global platform
global filesPresent


platform = 'Linux'.title() 	#Have wine or use Windows
DDLC_MASTER='DDLC-Master.zip'

try:
	file = open("Instances.dat","r")
	file.close()
	filesPresent = True
except FileNotFoundError:
	file = open("Instances.dat","w")
	file.close()
	filesPresent = False

if filesPresent:
	file = open("Instances.dat","r")
	instances = file.readlines()
	file.close()

def cls():
	if platform == 'Linux':
		os.system("clear")
	if platform == 'Windows':
		os.system("cls")

def play(instName):
	cls()
	try:
		os.chdir(instName)
		if platform == 'Linux':
			os.system("wine DDLC.exe")
		if platform == 'Windows':
			os.system("start DDLC.exe")
		os.chdir("..")
	except FileNotFoundError:
		print("That instance doesn't exist!")

def newInstance(name):
	print("Creating instance...")
	file = zipfile.ZipFile(DDLC_MASTER,'r')
	file.extractall(name)
	file.close()

	file=open("Instances.dat","a")
	file.write(name.replace("\n","")+"\n")
	file.close()
	cls()

def deleteInst(InstDel):
	file = open("Instances.dat","r")
	content = file.readlines()
	file.close()
	if platform=="Linux":
		os.system("rm -rf "+InstDel)
		os.system("rm Instances.dat")
	if platform=="Windows":
		os.system("DEL /F /A "+InstDel)
		os.system("Instances.dat")
	file = open("Instances.dat","w")
	for i in range(len(content)):
		if content[i]!=InstDel+"\n":
			file.write(content[i].replace("\n","")+"\n")
	file.close()
	cls()

cls()
while True:
	try:
		file = open("Instances.dat","r")
		file.close()
		filesPresent = True
	except FileNotFoundError:
		file = open("Instances.dat","w")
		file.close()
		filesPresent = False

	if filesPresent:
		file = open("Instances.dat","r")
		instances = file.readlines()
		file.close()

	print("Instances \n")
	if filesPresent and len(instances)>0:
		for i in range(len(instances)):
			print(instances[i].replace("\n",""))
	elif not(filesPresent) or len(instances)<=0:
		print("No instances detected!")
	x = input("\n:")
	if "PLAY" in x.upper():
		x = x.replace("play ","").strip()
		play(x)
	elif x.upper()=="E" or x.upper().strip()=="EXIT":
		exit()
	elif "NEW" in x.upper():
		x = x.replace("new ","").strip()
		newInstance(x)
	elif "DEL" in x.upper():
		x = x.replace("del ","").strip()
		deleteInst(x)
	else:
		cls()
