from genericpath import isfile
import re
import subprocess
import os

"""

	HaoZipLang changing function

"""
def langDll():
	dirPathDialog= "D:\\repos\\HaoZipTranslation\\lng\\en\\lang\\HaoZipLang_chs\\Dialog"
	dirPathPng= "D:\\repos\\HaoZipTranslation\\lng\\en\\lang\\HaoZipLang_chs\\PNG"
	dirPathString= "D:\\repos\\HaoZipTranslation\\lng\\en\\lang\HaoZipLang_chs\\String"
	dirPathMenu= "D:\\repos\\HaoZipTranslation\\lng\\en\\lang\\HaoZipLang_chs\\Menu"

	dirPathBMP= "D:\\repos\\HaoZipTranslation\\lng\\en\\HaoZip\\Bitmap"

	dirHaoCDDialog ="D:\\repos\\HaoZipTranslation\\lng\\en\\HaoZipCD\\Dialog"
	dirHaoCDString ="D:\\repos\\HaoZipTranslation\\lng\\en\\HaoZipCD\\String"

	workPath = "D:\\repos\\temp"
	
	resDialog = getFiles(dirPathDialog)
	resPng = getFiles(dirPathPng)
	resString = getFiles(dirPathString)
	resMenu = getFiles(dirPathMenu)
	resHaoBmp = getFiles(dirPathBMP)	
	resHaoCDDialog = getFiles(dirHaoCDDialog)
	resHaoCDString = getFiles(dirHaoCDString)


	# HaoZipLang_chs.dll
	setAssignLang(workPath,"Dialog",dirPathDialog,resDialog)
	setAssignLang(workPath,"PNG",dirPathPng,resPng)
	setAssignLang(workPath,"String",dirPathString,resString)
	setAssignLang(workPath,"Menu",dirPathMenu,resMenu)
	# HaoZip.exe
	setAssignHaoCD(workPath,"String",dirHaoCDString,resHaoCDString)
	setAssignHaoCD(workPath,"Dialog",dirHaoCDDialog,resHaoCDDialog)
	# HaoZipCD.exe
	setAssignHao(workPath,dirPathBMP,resHaoBmp)



def setAssignLang(workPath,type,dirPath,res):
	for x in res:
		print(x)
		if type == "String":
			subprocess.run(f'Restorator.exe -open "{workPath}\\lang\\HaoZipLang_chs.dll" -nobackup -delete String -assign "{dirPath}\\{x}" -save -exit')
		else:
			subprocess.run(f'Restorator.exe -open "{workPath}\\lang\\HaoZipLang_chs.dll" -nobackup -delete {type}\{x[:-3]} -assign "{dirPath}\\{x}" -save -exit')


def setAssignHaoCD(workPath,type,dirPath,res):
	for x in res:
		print(x)
		if type == "String":
			subprocess.run(f'Restorator.exe -open "{workPath}\\HaoZipCD.exe" -nobackup -delete String -assign "{dirPath}\\{x}" -save -exit')
		else:
			subprocess.run(f'Restorator.exe -open "{workPath}\\HaoZipCD.exe" -nobackup -delete {type}\{x[:-3]} -assign "{dirPath}\\{x}" -save -exit')


def setAssignHao(workPath,dirPath,res):
	for x in res:
		print(x)
		subprocess.run(f'Restorator.exe -open "{workPath}\\HaoZip.exe" -nobackup -assign "{dirPath}\\{x}" -save -exit')



def getFiles(dirPath):
	res = []
	for path in os.listdir(dirPath):
		if os.path.isfile(os.path.join(dirPath,path)):
			res.append(path)
	return res



langDll()
