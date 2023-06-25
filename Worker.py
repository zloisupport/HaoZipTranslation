import os
import shutil
import codecs

from dotenv import load_dotenv



archs = ["32", "64"]
languages = ["ru", "en"]
        

class ConvertCommand():
    def __init__(self,directory,base_encoding="utf-8",to_encoding="cp1251") -> None:
        self.directory=directory
        self.base_encoding=base_encoding
        self.to_encoding=to_encoding
        print("-----------__INIT__----------------")
        print(self.base_encoding , self.to_encoding)
        print("-----------------------------------")

    
    def execute(self):
        # We get a list of files in the directory
        files = os.listdir(self.directory)

        # We go through each file in the list
        for filename in files:
            print(filename)
            # Check that the file has an extension .rc
            if filename.endswith('.rc'):
                # Open the file in the current encoding and read its contents
                with codecs.open(os.path.join(self.directory, filename), 'r',  self.base_encoding) as f:
                    content = f.read()
                # Open the file in the UTF-8 encoding and write an attached content into it
                with codecs.open(os.path.join(self.directory, filename), 'w', self.to_encoding) as f:
                    f.write(content)


class ClearCommand:
    def __init__(self, path):
        self.path = path
        self.remove_files =["2345Uninst.exe", "HaoZipUpdate.exe", "Uninstall.exe",
                            "HaoZipHomePage.exe", "HaoZipAce32Loader.exe", "Haozip_2345Upgrade.exe",
                            "Haozip_2345Upgrade.dll", "pic", "Protect", "tool"]

    
    def execute(self):
        for lng in languages:
            for arch in archs:
                for rmfile in self.remove_files:
                    file_path = os.path.join(self.path,f"{lng}//{arch}//{rmfile}")
                    print(file_path)
                    if os.path.isfile(file_path):
                        os.remove(file_path)
                    elif os.path.exists(file_path):
                        shutil.rmtree(file_path)

class CopyCommand:
    def __init__(self, src_path, dest_path):
        self.src_path = src_path
        self.dest_path = dest_path
    
    def execute(self):
        for lng in languages:
            if os.path.exists(os.path.join(f"{self.src_path}/x32/", f"lang/HaoZipLang_chs.dll")):
                shutil.copy(os.path.join(f"{self.src_path}/x32/", f"lang/HaoZipLang_chs.dll"),
                            os.path.join(f"{self.dest_path}/", f"{lng}"))
            for arch in archs:
               if os.path.exists(f"{self.src_path}/x{arch}"):
                   shutil.copytree(f"{self.src_path}/x{arch}/", f"{self.dest_path}/{lng}/{arch}", dirs_exist_ok=True)

class BuildCopyCommand:
    def __init__(self, current_directory, dest_haozip_path, dest_files_path):
        self.current_directory = current_directory
        self.dest_haozip_path = dest_haozip_path
        self.dest_files_path = dest_files_path
    
    def execute(self):
        tools = ("HaoZipMd5.exe", "HaoZipRename.exe", "HaoZipReplace.exe", "HaoZipCD.exe")
        drivers = ("HaoZipVirtualCDBus.cat", "HaoZipVirtualCDBus.inf", "HaoZipVirtualCDBus.sys")

        app_x64_files = [
                "7zNew.data",
                "2345DirectUI.dll",
                "api-ms-win-core-console-l1-1-0.dll",
                "api-ms-win-core-datetime-l1-1-0.dll",
                "api-ms-win-core-debug-l1-1-0.dll",
                "api-ms-win-core-errorhandling-l1-1-0.dll",
                "api-ms-win-core-file-l1-1-0.dll",
                "api-ms-win-core-file-l1-2-0.dll",
                "api-ms-win-core-file-l2-1-0.dll",
                "api-ms-win-core-handle-l1-1-0.dll",
                "api-ms-win-core-heap-l1-1-0.dll",
                "api-ms-win-core-interlocked-l1-1-0.dll",
                "api-ms-win-core-libraryloader-l1-1-0.dll",
                "api-ms-win-core-localization-l1-2-0.dll",
                "api-ms-win-core-memory-l1-1-0.dll",
                "api-ms-win-core-namedpipe-l1-1-0.dll",
                "api-ms-win-core-processenvironment-l1-1-0.dll",
                "api-ms-win-core-processthreads-l1-1-0.dll",
                "api-ms-win-core-processthreads-l1-1-1.dll",
                "api-ms-win-core-profile-l1-1-0.dll",
                "api-ms-win-core-rtlsupport-l1-1-0.dll",
                "api-ms-win-core-string-l1-1-0.dll",
                "api-ms-win-core-synch-l1-1-0.dll",
                "api-ms-win-core-synch-l1-2-0.dll",
                "api-ms-win-core-sysinfo-l1-1-0.dll",
                "api-ms-win-core-timezone-l1-1-0.dll",
                "api-ms-win-core-util-l1-1-0.dll",
                "api-ms-win-crt-conio-l1-1-0.dll",
                "api-ms-win-crt-convert-l1-1-0.dll",
                "api-ms-win-crt-environment-l1-1-0.dll",
                "api-ms-win-crt-filesystem-l1-1-0.dll",
                "api-ms-win-crt-heap-l1-1-0.dll",
                "api-ms-win-crt-locale-l1-1-0.dll",
                "api-ms-win-crt-math-l1-1-0.dll",
                "api-ms-win-crt-multibyte-l1-1-0.dll",
                "api-ms-win-crt-private-l1-1-0.dll",
                "api-ms-win-crt-process-l1-1-0.dll",
                "api-ms-win-crt-runtime-l1-1-0.dll",
                "api-ms-win-crt-stdio-l1-1-0.dll",
                "api-ms-win-crt-string-l1-1-0.dll",
                "api-ms-win-crt-time-l1-1-0.dll",
                "api-ms-win-crt-utility-l1-1-0.dll",
                "Benchmark.data",
                "HaoZip.dll",
                "HaoZipC.exe",
                "HaozipCD.dll",
                "HaoZipCom.dll",
                "HaoZipCom32.dll",
                "HaoZipEditor.dll",
                "HaoZipExt.dll",
                "HaoZipExt32.dll",
                "HaoZipFormats.dll",
                "HaoZipLoader.exe",
                "HaoZipLoader32.exe",
                "HaoZipTool.exe",
                "msvcp120.dll",
                "msvcp140.dll",
                "msvcr120.dll",
                "RarNew.data",
                "TarNew.data",
                "ucrtbase.dll",
                "vcruntime140.dll",
                "ZipNew.data"
        ]

        for arch in archs:
            for lng in languages:
                shutil.copy(os.path.join(self.current_directory, f"{lng}/{arch}/HaoZip.exe"),
                            os.path.join(self.dest_haozip_path, f"x{arch}-{lng}"))
                shutil.copy(os.path.join(self.current_directory, f"{lng}/HaoZipLang_chs.dll"),
                            os.path.join(self.dest_files_path, f"lang/{lng}/lang"))

                for tool in tools:
                    if tool == "HaoZipCD.exe":
                        shutil.copy(os.path.join(self.current_directory, f"{lng}/{arch}/{tool}"),
                                    os.path.join(self.dest_haozip_path, f"x{arch}-app-tools/VirtualCD/{lng}"))
                    else:
                        shutil.copy(os.path.join(self.current_directory, f"{lng}/{arch}/{tool}"),
                                    os.path.join(self.dest_haozip_path, f"x{arch}-app-tools"))

                for driver in drivers:
                    shutil.copy(os.path.join(self.current_directory, f"{lng}/{arch}/{driver}"),
                                os.path.join(self.dest_haozip_path, f"x{arch}-app-tools/VirtualCD"))

                for x64_file in app_x64_files:
                    if os.path.exists(os.path.join(self.current_directory, f"{lng}/{arch}/{x64_file}")):
                        shutil.copy(os.path.join(self.current_directory, f"{lng}/{arch}/{x64_file}"),
                                    os.path.join(self.dest_haozip_path, f"x{arch}-app"))



class Invoker:
    def set_command(self, command):
        self.command = command
    
    def execute_command(self):
        self.command.execute()



def main():
    """main"""
    load_dotenv()
    dest_haozip_path = os.getenv("DEST_HAOZIP_PATH")
    dest_files_path = os.getenv("DEST_FILES_PATH")

    current_file = os.path.abspath(__file__)
    current_directory = os.path.dirname(current_file)
    print(current_directory)
    
    clear_command = ClearCommand(current_directory)
    copy_command = CopyCommand(current_directory, current_directory)  
    
    base_encoding = None
    to_encoding = None
    build_copy_command = BuildCopyCommand(current_directory, dest_haozip_path, dest_files_path)

    invoker = Invoker()


    while True:
        user_input = input("""Введите команду
          (0-exit/
          1-clear/
          2-copy/
          3-build/
          4-convert): """)
        if user_input == "0":
            exit()
        if user_input == "1":
            invoker.set_command(clear_command)
            invoker.execute_command()
        if user_input == "2":
            invoker.set_command(copy_command)
            invoker.execute_command()
        if user_input == "3":
            invoker.set_command(build_copy_command)
            invoker.execute_command()
        if user_input == "4":
            print("1 = utf -cp1251 2= cp1251-utf")
            enc_input = input(":")
            if enc_input == "1":
                base_encoding = "utf-8"
                to_encoding = "cp1251"
            if enc_input == "2":
                base_encoding = "cp1251"
                to_encoding = "utf-8"
            print(base_encoding,to_encoding)
            convert_command = ConvertCommand(os.path.join(os.getenv("LOCAL_FILES_PATH"), "lng/ru/lang/HaoZipLang_chs/Dialog"),base_encoding=base_encoding,to_encoding=to_encoding)
            invoker.set_command(convert_command)
            invoker.execute_command()
            
if __name__ == "__main__":
    main()
