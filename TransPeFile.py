from genericpath import isfile
import re
import subprocess
import os
import json
"""

	HaoZipLang changing function

"""
def langDll(path,lang,workdir):
	dirPathDialog= f"{path}\\lng\\{lang}\\lang\\HaoZipLang_chs\\Dialog"


	print(dirPathDialog)
	dirPathPng= f"{path}\\lng\\{lang}\\lang\\HaoZipLang_chs\\PNG"
	dirPathString= f"{path}\\lng\\{lang}\\lang\HaoZipLang_chs\\String"
	dirPathMenu= f"{path}\\lng\\{lang}\\lang\\HaoZipLang_chs\\Menu"

	dirPathBMP= f"{path}\\lng\\{lang}\\HaoZip\Bitmap"

	dirHaoCDDialog =f"{path}\\lng\\{lang}\\HaoZipCD\\Dialog"
	dirHaoCDString =f"{path}\\lng\\{lang}\\HaoZipCD\\String"

	
	resDialog = getFiles(dirPathDialog)
	resPng = getFiles(dirPathPng)
	resString = getFiles(dirPathString)
	resMenu = getFiles(dirPathMenu)
	resHaoBmp = getFiles(dirPathBMP)	
	resHaoCDDialog = getFiles(dirHaoCDDialog)
	resHaoCDString = getFiles(dirHaoCDString)


	# HaoZipLang_chs.dll
	setAssignLang(workdir,"Dialog",dirPathDialog,resDialog)
	setAssignLang(workdir,"PNG",dirPathPng,resPng)
	setAssignLang(workdir,"String",dirPathString,resString)
	setAssignLang(workdir,"Menu",dirPathMenu,resMenu)
	# HaoZip.exe
	setAssignHaoCD(workdir,"String",dirHaoCDString,resHaoCDString)
	setAssignHaoCD(workdir,"Dialog",dirHaoCDDialog,resHaoCDDialog)
	# HaoZipCD.exe
	setAssignHao(workdir,dirPathBMP,resHaoBmp)



def setAssignLang(workdir,type,dirPath,res):
	for x in res:
		print(x)
		if type == "String":
			subprocess.run(f'Restorator.exe -open "{workdir}\\lang\\HaoZipLang_chs.dll" -nobackup -delete String -assign "{dirPath}\\{x}" -save -exit')
		else:
			subprocess.run(f'Restorator.exe -open "{workdir}\\lang\\HaoZipLang_chs.dll" -nobackup -delete {type}\{x[:-3]} -assign "{dirPath}\\{x}" -save -exit')


def setAssignHaoCD(workdir,type,dirPath,res):
	for x in res:
		print(x)
		if type == "String":
			subprocess.run(f'Restorator.exe -open "{workdir}\\HaoZipCD.exe" -nobackup -delete String -assign "{dirPath}\\{x}" -save -exit')
		else:
			subprocess.run(f'Restorator.exe -open "{workdir}\\HaoZipCD.exe" -nobackup -delete {type}\{x[:-3]} -assign "{dirPath}\\{x}" -save -exit')


def setAssignHao(workdir,dirPath,res):
	for x in res:
		print(x)
		subprocess.run(f'Restorator.exe -open "{workdir}\\HaoZip.exe" -nobackup -assign "{dirPath}\\{x}" -save -exit')



def getFiles(dirPath):
	res = []
	for file in os.listdir(dirPath):
		if os.path.isfile(os.path.join(dirPath,file)):
			res.append(file)
	return res

if __name__ == "__main__":
	confFile = "conf.json"
	if not os.path.exists(confFile):
		print('conf.json: not found')
		defaultData ={"path":"D:\\repos\\HaoZipTranslation", "lang": "en", "workdir":"D:\\repos\\temp"}
		
		print('creatig: conf.json ')
		with open("conf.json","w",) as outFile:
			json.dump(defaultData,outFile,indent=4)
			outFile.close
	else:
		print('read: conf.json ')
		data = json.load(open(confFile,'r'))

		path = data['path']
		lang = data['lang']
		workdir = data['workdir']
		print(f'conf: {path,lang,workdir}')
		langDll(path,lang,workdir)
