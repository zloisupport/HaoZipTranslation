**Option -r (Recursively Scan Subdirectories)**

--------------------------------------------------------------------------------

Specifies how masks and filenames in the command line should be processed.

**Syntax**

`-r[- | 0]`

| Option | Description                                                                                                                                                                                                                                                                         |
|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `-r`   | Enable recursive traversal of subdirectories. This option is used by default for commands working with files in the archive, such as `e` (extract), `l` (list), `t` (test), `x` (extract with full path).                                                                             |
| `-r-`  | Disable recursive traversal of subdirectories. This option is used by default for all commands that need to scan files on disk, such as `a` (add), `d` (delete), `u` (update).                                                                                                  |
| `-r0` | Enable recursive traversal of subdirectories. But this only applies to masks.                                                                                                                                                                                                   |

**Examples**

`HaoZipC l archive.zip -r- *.doc`: List the `*.doc` files located in the root directory of the `archive.zip` archive.

`HaoZipC a -tzip archive.zip -r src\*.cpp src\*.h`: Add `*.cpp` and `*.h` files from the `src` directory and its subdirectories to the `archive.zip` archive.

**Options that can be used with this option:** `a` (add), `d` (delete), `e` (extract), `t` (test), `u` (update), `x` (extract with full path).
