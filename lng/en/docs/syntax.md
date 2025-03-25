**Syntax a (Add command)**

Command for adding files to an archive.

Example: `HaoZipC a -tzip archive.zip subdir\*` - adds all files from the `subdir` folder to the `archive.zip` archive. `HaoZipC a -tzip Files.zip "Program files\*" -r` - adds all files from the `Program files` folder to the `Files.zip` archive.

Options that can be used with this command: `-i` (include filenames), `-m` (set compression algorithm), `-p` (set password), `-r` (recursively scan subdirectories), `-t` (set archive format), `-u` (update options), `-w` (set working directory), `-x` (exclude files).

Other commands: `d` (delete), `u` (update).

**Syntax d (Delete command)**

Deleting files from an archive.

Example: `HaoZipC d archive.zip *.bak` - deletes `*.bak` files from the `archive.zip` archive.

Options that can be used with this command: `-i` (include filenames), `-m` (set compression algorithm), `-p` (set password), `-r` (recursively scan subdirectories), `-u` (update options), `-w` (set working directory), `-x` (exclude files).

Other commands: `a` (add), `u` (update).

Other options: `-u` (update options).

**Syntax e (Extract command)**

Extracting files from an archive to the current directory or to the specified output folder. The output folder can be changed using the `-o` option (set output folder).

This command places all extracted files into a single folder. If you want to extract files preserving the full path, you must use the `x` command (extract with full path).

When overwriting existing files, the user will be prompted to select the next action. This will not happen if the user specifies the `-y` option (always).

The following responses are supported:

| Response      | Abbreviation | Description                                 |
|---------------|--------------|---------------------------------------------|
| Yes           | y            |                                             |
| No            | n            |                                             |
| Always        | a            | Answer YES to all requests                   |
| Skip          | s            | Answer NO to all requests                    |
| Quit          | q            | Exit the program                            |

Example: `HaoZipC e archive.zip` - extracts all files from the `archive.zip` archive to the current folder. `HaoZipC e archive.zip -oc:\soft *.cpp` - extracts `*.cpp` files from the `archive.zip` archive to the `c:\soft` folder.

Options that can be used with this command: `-ao` (overwrite mode), `-i` (include filenames), `-o` (set output directory), `-p` (set password), `-r` (recursively scan subdirectories), `-x` (exclude files), `-y` (always).

Other commands: `x` (extract with full path).

**Syntax l (List command)**

Displaying the contents of an archive.

Example: `HaoZipC l archive.zip` - displays the contents of the `archive.zip` archive.

Options that can be used with this command: `-i` (include filenames), `-r` (recursively scan subdirectories), `-x` (exclude files).

**Syntax t (Test command)**

Testing the integrity of an archive.

Example: `HaoZipC t archive.zip *.doc` - tests the integrity of `*.doc` files in the `archive.zip` archive.

Options that can be used with this command: `-i` (include filenames), `-r` (recursively scan subdirectories), `-p` (set password), `-x` (exclude files).

**Syntax u (Update command)**

Replacing older files in an archive with newer files.

Example: `HaoZipC u archive.zip *.doc` - updates `*.doc` files in the `archive.zip` archive.

Options that can be used with this command: `-i` (include filenames), `-m` (set compression algorithm), `-p` (set password), `-r` (recursively scan subdirectories), `-t` (set archive format), `-u` (update options), `-w` (set working directory), `-x` (exclude files).

Other commands: `a` (add), `d` (delete).

Other options: `-u` (update options).

**Syntax x (Extract with Full Path command)**

Extracting files from an archive, preserving the full path, to the current directory or to the specified output folder. For more information, see the description of the `e` command (extract).

Example: `HaoZipC x archive.zip` - extracts all files from the `archive.zip` archive to the current folder, preserving the full path. `HaoZipC x archive.zip -oc:\soft *.cpp` - extracts `*.cpp` files from the `archive.zip` archive to the `c:\soft` folder, preserving the full path.

Options that can be used with this command: `-ao` (overwrite mode), `-i` (include filenames), `-o` (set output directory), `-p` (set password), `-r` (recursively scan subdirectories), `-x` (exclude files), `-y` (always).

Other commands: `e` (extract).
