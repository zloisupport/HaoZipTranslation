from genericpath import isfile
import re
import subprocess
import os
import json

"""

	HaoZipLang changing function

"""


def langDll(path, lang, workdirs):
    dirPathDialog = f"{path}\\lng\\{lang}\\lang\\HaoZipLang_chs\\Dialog"
    dirPathPng = f"{path}\\lng\\{lang}\\lang\\HaoZipLang_chs\\PNG"
    dirPathString = f"{path}\\lng\\{lang}\\lang\HaoZipLang_chs\\String"
    dirPathMenu = f"{path}\\lng\\{lang}\\lang\\HaoZipLang_chs\\Menu"
    dirPathBMP = f"{path}\\lng\\{lang}\\HaoZip\Bitmap"

    transFiles = [dirPathDialog,dirPathPng,dirPathString,dirPathMenu,dirPathBMP]

    for file in transFiles:
        if not os.path.exists(file):
            raise FileExistsError(file) 

    dirHaoCDDialog = f"{path}\\lng\\{lang}\\HaoZipCD\\Dialog"
    dirHaoCDString = f"{path}\\lng\\{lang}\\HaoZipCD\\String"

    resDialog = getFiles(dirPathDialog)
    resPng = getFiles(dirPathPng)
    resString = getFiles(dirPathString)
    resMenu = getFiles(dirPathMenu)
    resHaoBmp = getFiles(dirPathBMP)
    resHaoCDDialog = getFiles(dirHaoCDDialog)
    resHaoCDString = getFiles(dirHaoCDString)
    count = 0
    for workdir in workdirs:

        # HaoZipCD.exe
        setAssignHaoCD(workdir, "String", dirHaoCDString, resHaoCDString)
        setAssignHaoCD(workdir, "Dialog", dirHaoCDDialog, resHaoCDDialog)
        #  HaoZip.exe
        setAssignHao(workdir, dirPathBMP, resHaoBmp)

        # HaoZipLang_chs.dll
        count = count + 1
        if count == 1:
            setAssignLang(workdir, "Dialog", dirPathDialog, resDialog)
            setAssignLang(workdir, "PNG", dirPathPng, resPng)
            setAssignLang(workdir, "String", dirPathString, resString)
            setAssignLang(workdir, "Menu", dirPathMenu, resMenu)


def setAssignLang(workdir, type, dirPath, res):
    if os.path.exists(f"{workdir[:len(workdir) - 2]}\\HaoZipLang_chs.dll"):
        for x in res:
            if type == "String":
                subprocess.run(
                    f'Restorator.exe -open "{workdir[:len(workdir) - 2]}\\HaoZipLang_chs.dll" -nobackup -delete String -assign "{dirPath}\\{x}" -save -exit')
            else:
                subprocess.run(
                    f'Restorator.exe -open "{workdir[:len(workdir) - 2]}\\HaoZipLang_chs.dll" -nobackup -delete {type}\{x[:-3]} -assign "{dirPath}\\{x}" -save -exit')


def setAssignHaoCD(workdir, type, dirPath, res):
    if os.path.exists(f"{workdir}\\HaoZipCD.exe"):
        for x in res:
            print(x)
            if type == "String":
                subprocess.run(
                    f'Restorator.exe -open "{workdir}\\HaoZipCD.exe" -nobackup -delete String -assign "{dirPath}\\{x}" -save -exit')
            else:
                subprocess.run(
                    f'Restorator.exe -open "{workdir}\\HaoZipCD.exe" -nobackup -delete {type}\{x[:-3]} -assign "{dirPath}\\{x}" -save -exit')


def setAssignHao(workdir, dirPath, res):
    if os.path.exists(f"{workdir}\\HaoZip.exe"):
        for x in res:
            print(x)
            subprocess.run(f'Restorator.exe -open "{workdir}\\HaoZip.exe" -nobackup -assign "{dirPath}\\{x}" -save -exit')


def getFiles(dirPath):
    res = []
    for file in os.listdir(dirPath):
        if os.path.isfile(os.path.join(dirPath, file)):
            res.append(file)
    return res


def createWorkDir(dir_paths):
    for dir_path in dir_paths:
        if not os.path.exists(dir_path):
            print("Creating Empty Project folder!")
            os.makedirs(dir_path)
            raise UserWarning("Project folder empty!")


def main():
    confFile = "conf.json"
    if not os.path.exists(confFile):
        print('conf.json: not found')
        defaultData = {
            "path": "D:\\repos\\HaoZipTranslation",
            "workdir": "D:\\repos\\temp",
            "lang": {
                "ru": {
                    "x64": "64",
                    "x32": "32"
                },
                "en": {
                    "x64": "64",
                    "x32": "32"
                }
            }
        }

        print('creatig: conf.json ')
        with open("conf.json", "w", ) as outFile:
            json.dump(defaultData, outFile, indent=4)
            outFile.close
    else:
        print('read: conf.json ')
        data = json.load(open(confFile, 'r'))

        path = data['path']
        workDir = data['workdir']

        for lang, values in data['lang'].items():
            for arch in values.values():
                dir_paths = [f'{workDir}/{lang}/{arch}']
                createWorkDir(dir_paths)
                langDll(path, lang, dir_paths)

if __name__ == "__main__":
    main()