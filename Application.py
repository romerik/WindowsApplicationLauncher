#coding:utf-8
import os
try:
	open('file.txt','r')
except:
	for i in ['C:\\']:
		os.system("dir /s /b \""+i+"\"*.exe > file.txt")
def comline(m,path):
	for i in path:
		if m.upper() in i.upper():
			i="\""+i.replace('\n','')+"\""
			try:
				os.system(i)
			except:
				pass
path= os.environ['PATH'].split(';')
fichier = open('file.txt','r')
path+=fichier.readlines()
fichier.close()
cmd=input("Enter the name:")
if not cmd.endswith(".exe"):
	cmd= cmd +".exe"
comline(cmd,path)