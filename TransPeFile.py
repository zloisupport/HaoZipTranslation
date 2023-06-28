from genericpath import isfile
import re
import subprocess
import os
import json
import time
"""

	HaoZipLang changing function

"""
count = 0
RESTORATOR_FILE_BACKUP = '-nobackup'


def langDll(path, lang, workdirs):
    root_dir = f'{path}\lng\{lang}'
    work_dir_lng = f'{workdirs[0][:len(workdirs[0])-3]}{lang}'
    root_HaoZipLang_chs = f'{root_dir}\lang\HaoZipLang_chs'

    res_path_BMP = f"{root_dir}\HaoZip\Bitmap"
    res_HaoCD_Dialog = f"{root_dir}\HaoZipCD\Dialog"
    res_HaoCD_String = f"{root_dir}\HaoZipCD\String"

    res_path_Dialog = f"{root_HaoZipLang_chs}\Dialog"
    res_path_Png = f"{root_HaoZipLang_chs}\PNG"
    res_path_String = f"{root_HaoZipLang_chs}\String"
    res_path_Menu = f"{root_HaoZipLang_chs}\Menu"


    trans_files = [res_path_Dialog,res_path_Png,res_path_String,res_path_Menu,res_path_BMP]

    for file in trans_files:
        if not os.path.exists(file):
            raise FileExistsError(file) 

    resDialog = getFiles(res_path_Dialog)
    resPng = getFiles(res_path_Png)
    resString = getFiles(res_path_String)
    resMenu = getFiles(res_path_Menu)
    resHaoBmp = getFiles(res_path_BMP)
    resHaoCDDialog = getFiles(res_HaoCD_Dialog)
    resHaoCDString = getFiles(res_HaoCD_String)

    # HaoZipLang_chs.dll
    # To prevent the loop from running four 
    global count
    count+=1
    if count == 2:
        setAssignLang(work_dir_lng, "Dialog", res_path_Dialog, resDialog)
        setAssignLang(work_dir_lng, "PNG", res_path_Png, resPng)
        setAssignLang(work_dir_lng, "String", res_path_String, resString)
        setAssignLang(work_dir_lng, "Menu", res_path_Menu, resMenu)
        count =0

    for workdir in workdirs:
        print(workdir)
        # HaoZipCD.exe
        setAssignHaoCD(workdir, "String", res_HaoCD_String, resHaoCDString)
        setAssignHaoCD(workdir, "Dialog", res_HaoCD_Dialog, resHaoCDDialog)
        #  HaoZip.exe
        setAssignHao(workdir, res_path_BMP, resHaoBmp)



def setAssignLang(workdir, res_type, res_path, resourse):
    print(f"""HaoZipLang_chs.dll
    Open "{workdir[:len(workdir) - 2]}\HaoZipLang_chs.dll"
    Locate: {workdir[:len(workdir) - 2]}
    DirPath: {res_path}
    Type:{res_type}""")
    if os.path.exists(f"{workdir[:len(workdir) - 2]}\HaoZipLang_chs.dll"):
       if res_type == "String":
            for res in resourse:
                subprocess.run(
                    f'Restorator.exe -open "{workdir[:len(workdir) - 2]}\HaoZipLang_chs.dll" -nobackup -delete String -assign "{res_path}\{res}" -save -exit')
       else:
                subprocess.run(
                        f'Restorator.exe -open "{workdir[:len(workdir) - 2]}\HaoZipLang_chs.dll" -nobackup -assignOn "{res_type}" "{res_path}" -save -exit')


def setAssignHaoCD(workdir, res_type, res_path, resourse):
    if os.path.exists(f"{workdir}\HaoZipCD.exe"):
        print(f"""HaoZipCD.exe
        Workdir: {workdir}
        Res: {resourse}""")
        for res in resourse:
            if res_type == "String":
                subprocess.run(
                    f'Restorator.exe -open "{workdir}\HaoZipCD.exe" {RESTORATOR_FILE_BACKUP} -delete String -assign "{res_path}\{res}" -save -exit')
            else:
                subprocess.run(
                    f'Restorator.exe -open "{workdir}\HaoZipCD.exe" {RESTORATOR_FILE_BACKUP} -delete {res_type}\{res[:-3]} -assign "{res_path}\{res}" -save -exit')


def setAssignHao(workdir, res_path, res):
    if os.path.exists(f"{workdir}\HaoZip.exe"):
        for x in res:
            print(x)
            subprocess.run(f'Restorator.exe -open "{workdir}\HaoZip.exe" {RESTORATOR_FILE_BACKUP} -assign "{res_path}\{x}" -save -exit')


def getFiles(res_path):
    res = []
    for file in os.listdir(res_path):
        if os.path.isfile(os.path.join(res_path, file)):
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
    start_time = time.time()
    main()
    end_time = time.time()
    exec_time = end_time - start_time
    print(f"Execution time: {exec_time} sec")