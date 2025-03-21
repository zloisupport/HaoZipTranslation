import datetime
from enum import Enum
import shutil
import codecs
import subprocess
import os
import json
from subprocess import SubprocessError
from typing import Dict

RES_TOOL_EXE = "Restorator.exe"
OPEN_ARG = " -open"
FILE_BACKUP_ARG = '-nobackup'
FILE_SAVE_ARG = "-save"
EXIT_ARG = "-exit"

LANG_DLL_FILE = "HaoZipLang_chs.dll"
HAO_EXE_FILE = "HaoZip.exe"
HAO_CD_EXE_FILE = "HaoZipCD.exe"

HAO_FILES = [
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

class ModelMeta(type):
    def __new__(cls, name, bases, dct):
        dct['langs'] = {}
        dct['work_dir'] = None
        dct['translation_files'] = None
        dct['count'] = 0
        dct['app_paths'] = 0
        return super().__new__(cls, name, bases, dct)

class Model(metaclass=ModelMeta):
    langs: Dict[str, Dict[str, str]]
    work_dir: str
    translation_files: str
    count: int
    app_paths: int

    def __init__(self):
        self.langs = []
        self.work_dir = None
        self.translation_files = None
        self.count = 0
        self.app_paths = 0
        self.arch = []
        self.source_exe = ""

    def load_config(self, config_file="conf.json"):
        if not os.path.exists(config_file):
            print('conf.json: not found')
            default_data = {
                "path": "D:\\repos\\HaoZipTranslation",
                "workdir": "D:\\repos\\temp",
                "lang": ["ru", "en"],
                "arch": [32, 64]
            }

            with open(config_file, "w") as file:
                json.dump(default_data, file, indent=4)

            print('Created: conf.json')
        else:
            data = json.load(open(config_file, 'r'))

            self.work_dir = str(data['workdir'])
            self.translation_files = str(data['path'])
            self.langs = data['langs']
            self.arch = data['arch']
            self.source_exe = f'{self.work_dir}\\source_exe'

    def create_work_dir(self):
        for arch in self.arch:
            dir_path = os.path.join(self.source_exe, arch)
            if not os.path.exists(dir_path):
                print("Creating Empty Project folder!")
                os.makedirs(dir_path)

    @staticmethod
    def get_files(res_path) -> list[str]:
        res = []
        for file in os.listdir(res_path):
            if os.path.isfile(os.path.join(res_path, file)):
                res.append(file)
        return res

class ResType(Enum):
    Dialog = 1
    PNG = 2
    String = 3
    Menu = 4
    Bitmap = 5

class TranslatePeFileCommand(Model, metaclass=ModelMeta):
    def __init__(self):
        super().__init__()
        super().load_config()
        super().create_work_dir()

    @staticmethod
    def validate_path_exists(self, path: str):
        if not os.path.exists(path):
            raise FileExistsError(f"404:{path}")

    @staticmethod
    def validate_files_exists(self, res_paths: dict):
        for file in res_paths.values():
            self.validate_path_exists(file)

    @staticmethod
    def get_sub_folder(path):
        return [entry.name for entry in os.scandir(path) if entry.is_dir()]

    @staticmethod
    def checking_name_istype(path, subfolder):
        return {res_type: os.path.join(path, folder) for folder in subfolder for res_type in ResType if
                folder == res_type.name}

    def get_resource_hao_lang(self, lang):
        root_dir = os.path.join(self.translation_files, "lng", lang)

        root_lang_chs = os.path.join(root_dir, "lang", "HaoZipLang_chs")
        res_sub_lang = self.get_sub_folder(root_lang_chs)
        res_lang = self.checking_name_istype(root_lang_chs, res_sub_lang)

        return res_lang

    def get_resource_hao_cd(self, lang):
        root_dir = os.path.join(self.translation_files, "lng", lang)

        root_lang_cd = os.path.join(root_dir, "HaoZipCD")
        res_sub_cd = self.get_sub_folder(root_lang_cd)
        res_lang_cd = self.checking_name_istype(root_lang_cd, res_sub_cd)
        return res_lang_cd

    def get_resource_hao(self, lang):
        root_dir = os.path.join(self.translation_files, "lng", lang)

        root_hao = os.path.join(root_dir, "HaoZip")
        res_sub_hao = self.get_sub_folder(root_hao)
        res_hao = self.checking_name_istype(root_hao, res_sub_hao)

        return res_hao

    def process_translate_hao_lang(self, lang, path):
        data_path = self.get_resource_hao_lang(lang)
        for res_key, res_path in data_path.items():
            self.set_assign_resource(str(path), res_key, LANG_DLL_FILE, str(res_path))

    def process_translate_hao_cd(self, lang, path):
        data_path = self.get_resource_hao_cd(lang)
        for res_key, res_path in data_path.items():
            for arch in self.arch:
                recourse_path = os.path.join(path, arch)
                self.set_assign_resource(str(recourse_path), res_key, HAO_CD_EXE_FILE, str(res_path))

    def process_translate_hao(self, lang, path):
        data_path = self.get_resource_hao(lang)
        for res_key, res_path in data_path.items():
            for arch in self.arch:
                recourse_path = os.path.join(path, arch)
                self.set_assign_resource(str(recourse_path), res_key, HAO_EXE_FILE, str(res_path))

    @staticmethod
    def set_assign_resource(path: str, res_type: ResType, exe_name: str, res_path: str):
        try:
            # print(f'{RES_TOOL_EXE} {OPEN_ARG} "{path}\\{exe_name}" {FILE_BACKUP_ARG} -delete  {res_type.name} -assign "{res_type.name}" "{res_path}" {FILE_SAVE_ARG} {EXIT_ARG}')
            subprocess.run(
                f'{RES_TOOL_EXE} {OPEN_ARG} "{os.path.join(path, exe_name)}" {FILE_BACKUP_ARG} -assignOn {res_type.name} "{res_path}" {FILE_SAVE_ARG} {EXIT_ARG}')
        except SubprocessError as err:
            print(err)

    def execute(self):
        for lang in self.langs:
            path = os.path.join(self.work_dir, lang)
            self.process_translate_hao_lang(lang, path)
            self.process_translate_hao(lang, path)
            self.process_translate_hao_cd(lang, path)


class InitCommand(Model, metaclass=ModelMeta):
    def __init__(self):
        super().__init__()
        super().load_config()
        super().create_work_dir()

    def execute(self):
        return


class CopyFilesToWorkSpace(Model, metaclass=ModelMeta):
    def __init__(self):
        super().__init__()
        super().load_config()
        super().create_work_dir()

    def copy_lang_file_to_work_space(self):
        res_path = set()
        for arch in self.arch:
            path_lang_file = os.path.join(self.source_exe, arch, "lang", LANG_DLL_FILE)
            for lang in self.langs:
                dest_dir = os.path.join(self.work_dir, lang)
                if dest_dir in res_path:
                    continue
                if os.path.exists(path_lang_file):
                    res_path.add(dest_dir)
                    shutil.copy(path_lang_file, self.work_dir)
                else:
                    print(f'File not found: {path_lang_file}')

    def copy_other_file_to_work_space(self):
        for arch in self.arch:
            for lang in self.langs:
                dest_dir = os.path.join(self.work_dir, lang, arch)
                for file in HAO_FILES:
                    path_file = os.path.join(self.source_exe, arch, file)
                    if os.path.exists(path_file):
                        shutil.copy(path_file, dest_dir)
                    else:
                        print(f'File not found: {path_file}')

    def execute(self):
        self.copy_lang_file_to_work_space()
        self.copy_other_file_to_work_space()


class ChangePeInfoCommand(Model, metaclass=ModelMeta):
    def __init__(self):
        super().__init__()
        super().load_config()
        super().create_work_dir()
        self.company = "HaoZip"
        self.legalCopyright = f"HaoZip(c) {datetime.datetime.now().year} haozip.2345.com"

    def process_change_pe_lang_dll(self):
        for lang in self.langs:
            lang_file = os.path.join(self.work_dir, lang, LANG_DLL_FILE)
            if os.path.exists(lang_file):
                subprocess.run(f'{RES_TOOL_EXE} -open {lang_file} -nobackup \
                            -verSetString Comments "HaoZipLang {lang} "\
                            -verSetString CompanyName "{self.company}"\
                            -verSetString FileDescription "HaoZipLang {lang}"\
                            -verSetString InternalName "HaoZipLang {lang}"\
                            -verSetString LegalCopyright "{self.legalCopyright}"\
                            -verSetString OriginalFilename "HaoZipLang_chs.dll"\
                            -verSetString ProductName "HaoZipLang {lang}"\
                            -save -exit')

    def process_change_other_files(self):
        for arch in self.arch:
            for lang in self.langs:
                for file in HAO_FILES:
                    ext_len = len(file) - 4
                    file_name = f'{file[:ext_len]} {lang} '

                    hao_file = os.path.join(self.work_dir, lang, arch, file)
                    if os.path.exists(hao_file):
                        subprocess.run(f'{RES_TOOL_EXE} -open {hao_file} -nobackup \
                                       -verSetString Comments "{file_name}"\
                                       -verSetString CompanyName "{self.company}"\
                                       -verSetString FileDescription "{file_name}"\
                                       -verSetString InternalName "{file_name}"\
                                       -verSetString LegalCopyright "{self.legalCopyright}"\
                                       -verSetString OriginalFilename "{file_name}"\
                                       -verSetString ProductName "{file_name}"\
                                       -save -exit')

    def execute(self):
        self.process_change_pe_lang_dll()
        self.process_change_other_files()


class UnpackOrignFilesCommand(Model, metaclass=ModelMeta):
    def __init__(self):
        super().__init__()
        super().load_config()
        super().create_work_dir()

    def unpack_exe_source(self):
        for arch in self.arch:
            dest_path = os.path.join(self.source_exe, arch)
            src_exe = input(f'Enter path Hao###{arch}.exe\nTo return to the menu, enter: 0\n')
            if src_exe == '0':
                return
            if os.path.exists(src_exe):
                subprocess.run(f'7z.exe x "{src_exe}" -o"{dest_path}"')

    def execute(self):
        self.unpack_exe_source()


class ConvertCommand(Model, metaclass=ModelMeta):
    def __init__(self) -> None:
        super().__init__()
        super().load_config()

        self.base_encoding = "utf-8"
        self.to_encoding = "cp1251"

    def execute(self):
        print("1 = utf -cp1251 2 = cp1251-utf\n ")
        enc_input = input(":")
        if enc_input == "1":
            self.base_encoding = "utf-8"
            self.to_encoding = "cp1251"
        if enc_input == "2":
            self.base_encoding = "cp1251"
            self.to_encoding = "utf-8"
        if enc_input == "0":
            return

        for lang in self.langs:
            dialog_path = os.path.join(self.translation_files, "lng", lang, "lang", "HaoZipLang_chs", "Dialog")
            files = self.get_files(dialog_path)
            for file in files:
                if file.endswith('.rc'):
                    with codecs.open(os.path.join(dialog_path, file), 'r', self.base_encoding) as f:
                        content = f.read()

                    with codecs.open(os.path.join(dialog_path, file), 'w', self.to_encoding) as f:
                        f.write(content)


class ClearHaoUtilsCommand(Model, metaclass=ModelMeta):
    def __init__(self):
        super().__init__()
        super().load_config()

        self.remove_files = ["2345Uninst.exe", "HaoZipUpdate.exe", "Uninstall.exe",
                             "HaoZipHomePage.exe", "HaoZipAce32Loader.exe", "Haozip_2345Upgrade.exe",
                             "Haozip_2345Upgrade.dll", "Install.data", "libcurl_x64.dll", "libcurl_x86.dll",
                             "HaoZipWorker.exe", "pic", "Protect", "tool", "$0", "$PLUGINSDIR", "$R0"]

    def clear_files(self):
        for arch in self.arch:
            for rm_file in self.remove_files:
                file_path = os.path.join(self.source_exe, arch, rm_file)
                if os.path.isfile(file_path):
                    os.remove(file_path)
                elif os.path.exists(file_path):
                    shutil.rmtree(file_path)
        print(f"Success\n {self.source_exe}")

    def execute(self):
        self.clear_files()


class BuildCopyCommand:
    pass
    # def __init__(self):
    #     self.dest_haozip_path = None
    #     self.dest_files_path = None
    #
    # def execute(self):
    #     tools = ("HaoZipMd5.exe", "HaoZipRename.exe", "HaoZipReplace.exe", "HaoZipCD.exe")
    #     drivers = ("HaoZipVirtualCDBus.cat", "HaoZipVirtualCDBus.inf", "HaoZipVirtualCDBus.sys")
    #
    #     app_x64_files = [
    #         "7zNew.data",
    #         "2345DirectUI.dll",
    #         "api-ms-win-core-console-l1-1-0.dll",
    #         "api-ms-win-core-datetime-l1-1-0.dll",
    #         "api-ms-win-core-debug-l1-1-0.dll",
    #         "api-ms-win-core-errorhandling-l1-1-0.dll",
    #         "api-ms-win-core-file-l1-1-0.dll",
    #         "api-ms-win-core-file-l1-2-0.dll",
    #         "api-ms-win-core-file-l2-1-0.dll",
    #         "api-ms-win-core-handle-l1-1-0.dll",
    #         "api-ms-win-core-heap-l1-1-0.dll",
    #         "api-ms-win-core-interlocked-l1-1-0.dll",
    #         "api-ms-win-core-libraryloader-l1-1-0.dll",
    #         "api-ms-win-core-localization-l1-2-0.dll",
    #         "api-ms-win-core-memory-l1-1-0.dll",
    #         "api-ms-win-core-namedpipe-l1-1-0.dll",
    #         "api-ms-win-core-processenvironment-l1-1-0.dll",
    #         "api-ms-win-core-processthreads-l1-1-0.dll",
    #         "api-ms-win-core-processthreads-l1-1-1.dll",
    #         "api-ms-win-core-profile-l1-1-0.dll",
    #         "api-ms-win-core-rtlsupport-l1-1-0.dll",
    #         "api-ms-win-core-string-l1-1-0.dll",
    #         "api-ms-win-core-synch-l1-1-0.dll",
    #         "api-ms-win-core-synch-l1-2-0.dll",
    #         "api-ms-win-core-sysinfo-l1-1-0.dll",
    #         "api-ms-win-core-timezone-l1-1-0.dll",
    #         "api-ms-win-core-util-l1-1-0.dll",
    #         "api-ms-win-crt-conio-l1-1-0.dll",
    #         "api-ms-win-crt-convert-l1-1-0.dll",
    #         "api-ms-win-crt-environment-l1-1-0.dll",
    #         "api-ms-win-crt-filesystem-l1-1-0.dll",
    #         "api-ms-win-crt-heap-l1-1-0.dll",
    #         "api-ms-win-crt-locale-l1-1-0.dll",
    #         "api-ms-win-crt-math-l1-1-0.dll",
    #         "api-ms-win-crt-multibyte-l1-1-0.dll",
    #         "api-ms-win-crt-private-l1-1-0.dll",
    #         "api-ms-win-crt-process-l1-1-0.dll",
    #         "api-ms-win-crt-runtime-l1-1-0.dll",
    #         "api-ms-win-crt-stdio-l1-1-0.dll",
    #         "api-ms-win-crt-string-l1-1-0.dll",
    #         "api-ms-win-crt-time-l1-1-0.dll",
    #         "api-ms-win-crt-utility-l1-1-0.dll",
    #         "Benchmark.data",
    #         "HaoZip.dll",
    #         "HaoZipC.exe",
    #         "HaozipCD.dll",
    #         "HaoZipCom.dll",
    #         "HaoZipCom32.dll",
    #         "HaoZipEditor.dll",
    #         "HaoZipExt.dll",
    #         "HaoZipExt32.dll",
    #         "HaoZipFormats.dll",
    #         "HaoZipLoader.exe",
    #         "HaoZipLoader32.exe",
    #         "HaoZipTool.exe",
    #         "msvcp120.dll",
    #         "msvcp140.dll",
    #         "msvcr120.dll",
    #         "RarNew.data",
    #         "TarNew.data",
    #         "ucrtbase.dll",
    #         "vcruntime140.dll",
    #         "ZipNew.data"
    #     ]

        # for arch in ARCHITECTURE:
        #     for lng in LANGUAGES:
        #
        #         if not os.path.exists(os.path.join(self.dest_haozip_path, f"x{arch}-{lng}")):
        #             os.makedirs(os.path.join(self.dest_haozip_path, f"x{arch}-{lng}"))
        #
        #         shutil.copy(os.path.join(self.current_directory, f"{lng}/{arch}/HaoZip.exe"),
        #                     os.path.join(self.dest_haozip_path, f"x{arch}-{lng}"))
        #
        #         if not os.path.exists(os.path.join(self.dest_files_path, f"lang/{lng}/lang")):
        #             os.makedirs(os.path.join(self.dest_files_path, f"lang/{lng}/lang"))
        #
        #         shutil.copy(os.path.join(self.current_directory, f"{lng}/{LANG_DLL_FILE}"),
        #                     os.path.join(self.dest_files_path, f"lang/{lng}/lang"))
        #
        #         for tool in tools:
        #             if tool == "HaoZipCD.exe":
        #                 if not os.path.exists(
        #                         os.path.join(self.dest_haozip_path, f"x{arch}-app-tools/VirtualCD/{lng}")):
        #                     os.makedirs(os.path.join(self.dest_haozip_path, f"x{arch}-app-tools/VirtualCD/{lng}"))
        #
        #                 shutil.copy(os.path.join(self.current_directory, f"{lng}/{arch}/{tool}"),
        #                             os.path.join(self.dest_haozip_path, f"x{arch}-app-tools/VirtualCD/{lng}"))
        #             else:
        #                 shutil.copy(os.path.join(self.current_directory, f"{lng}/{arch}/{tool}"),
        #                             os.path.join(self.dest_haozip_path, f"x{arch}-app-tools"))
        #
        #         for driver in drivers:
        #             shutil.copy(os.path.join(self.current_directory, f"{lng}/{arch}/{driver}"),
        #                         os.path.join(self.dest_haozip_path, f"x{arch}-app-tools/VirtualCD"))
        #
        #         for x64_file in app_x64_files:
        #             if os.path.exists(os.path.join(self.current_directory, f"{lng}/{arch}/{x64_file}")):
        #                 shutil.copy(os.path.join(self.current_directory, f"{lng}/{arch}/{x64_file}"),
        #                             os.path.join(self.dest_haozip_path, f"x{arch}-app"))


class Invoker:
    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def execute_command(self):
        self.command.execute()

def main():
    """main"""

    model = Model()
    model.load_config()

    translated_command = TranslatePeFileCommand()
    init_command = InitCommand()
    copy_orign_files = UnpackOrignFilesCommand()
    copy_to_workspace_command = CopyFilesToWorkSpace()
    change_pe_command = ChangePeInfoCommand()
    clear_hao_utils_command = ClearHaoUtilsCommand()
    convert_command = ConvertCommand()
    build_copy_command = BuildCopyCommand()

    invoker = Invoker()

    while True:
        user_input = input("""Enter Command
          000-clear console
          00-exit
          01-init folders
          02-unpack hao##.exe
          03-copy files to workspace
          04-change pe info
          1-delete hao utils
          2-build
          3-convert
          4-pack translate PE file
          : """)
        if user_input == "0":
            os.system('cls' if os.name == 'nt' else 'clear')
        if user_input == "00":
            exit()
        if user_input == "01":
            invoker.set_command(init_command)
            invoker.execute_command()
        if user_input == "02":
            invoker.set_command(copy_orign_files)
            invoker.execute_command()
        if user_input == "03":
            invoker.set_command(copy_to_workspace_command)
            invoker.execute_command()
        if user_input == "04":
            invoker.set_command(change_pe_command)
            invoker.execute_command()
        if user_input == "1":
            invoker.set_command(clear_hao_utils_command)
            invoker.execute_command()
        if user_input == "2":
            invoker.set_command(build_copy_command)
            invoker.execute_command()
        if user_input == "3":
            invoker.set_command(convert_command)
            invoker.execute_command()
        if user_input == "4":
            invoker.set_command(translated_command)
            invoker.execute_command()


if __name__ == "__main__":
    main()
