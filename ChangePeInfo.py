import subprocess

def main():
	fileList = [
		"HaoZip.dll",
		"HaoZip.exe",
		"HaoZipC.exe",
		"HaozipCD.dll",
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


	companyName = 	"HaoZip"
	LegalCopyright = 	"HaoZip.cc"
	for file in fileList:
		extLen = len(file)-4
		fileDescription = file[:extLen]

		subprocess.run(f'Restorator.exe -open {file} -nobackup \
			-verSetString Comments {fileDescription} \
			-verSetString CompanyName {companyName} \
			-verSetString FileDescription {fileDescription}\
			-verSetString InternalName {fileDescription}\
			-verSetString LegalCopyright {LegalCopyright}\
			-verSetString OriginalFilename {file}\
			-verSetString ProductName {fileDescription}  \
			-verSetString ProductVersion {fileDescription}  \
			-saveAs {file} -exit')
main()