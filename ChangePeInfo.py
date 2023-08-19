import json
import subprocess
import os

def readJson():
	confFile = "conf.json"
	if not os.path.exists(confFile):
		raise FileNotFoundError(confFile)
	
	print('read: conf.json ')
	data = json.load(open(confFile, 'r'))
	workDir = data['workdir']

	for lang, values in data['lang'].items():
		for arch in values.values():
			changePe(workDir,lang,arch)


def changePe(workDir=None,lang=None,arch=None):
	app_path = f"{workDir}\\{lang}\\{arch}"
	if not os.path.exists(app_path):
		raise FileNotFoundError(app_path)
	fileList = [
		"2345DirectUI.dll",
		"HaoZip.dll",
		"HaoZip.exe",
		"HaoZipC.exe",
		"HaozipCD.dll",
		"HaozipCD.exe",
		"HaoZipCom.dll",
		"HaoZipCom32.dll",
		"HaoZipEditor.dll",
		"HaoZipExt.dll",
		"HaoZipExt32.dll",
		"HaoZipFormats.dll",
		"HaoZipIcons.dll",
		"HaoZipLoader.exe",
		"HaoZipLoader32.exe",
		"HaoZipMd5.exe",
		"HaoZipRename.exe",
		"HaoZipReplace.exe",
		"HaoZipTool.exe",
	]

#  "Comments:haozip.2345.com
#  "CompanyName:2345.com
#  "FileDescription:HaoZipCD
#  "FileVersion:5.8.1.10606
#  "InternalName:HaoZipCD
#  "LegalCopyright:版权所有(c) 2016 2345.com
#  "OriginalFilename:HaoZipCD.dll
#  "ProductName:HaoZipCD
#  "ProductVersion:5.8


	productVersion = "6.4.0.11152"
	fileVersion = "6.4.0.11152"
	companyName = "HaoZip"
	legalCopyright = "HaoZip(c) 2023 haozip.2345.com"

	subprocess.run(f'Restorator.exe -open {workDir}\\{lang}\\HaoZipLang_chs.dll -nobackup \
			-verSetString Comments "HaoZipLang_chs {lang}"\
			-verSetString CompanyName "{companyName}"\
			-verSetString FileDescription "HaoZipLang_chs {lang}"\
			-verSetString InternalName "HaoZipLang_chs {lang}"\
			-verSetString LegalCopyright "{legalCopyright}"\
			-verSetString OriginalFilename "HaoZipLang_chs.dll"\
			-verSetString ProductName "HaoZipLang_chs {lang}"\
			-save -exit')
	
	for file in fileList:
		extLen = len(file)-4
		fileDescription = file[:extLen]+f" {lang}"

		subprocess.run(f'Restorator.exe -open {app_path}\\{file} -nobackup \
			-verSetString Comments "{fileDescription}"\
			-verSetString CompanyName "{companyName}"\
			-verSetString FileDescription "{fileDescription}"\
			-verSetString InternalName "{fileDescription}"\
			-verSetString LegalCopyright "{legalCopyright}"\
			-verSetString OriginalFilename "{file}"\
			-verSetString ProductName "{fileDescription}"\
			-save -exit')
		# -verSetString ProductVersion "{productVersion}"\
		# -verSetString FileVersion "{fileVersion}"\

def main():
	readJson()


if __name__ == "__main__":
	main()
