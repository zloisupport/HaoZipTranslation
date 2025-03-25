**Option -ao (Overwrite Mode)**

--------------------------------------------------------------------------------

Specifies how to overwrite existing files with the same name on the disk during extraction.

**Syntax**

`-ao[a | s | u | t]`

| Parameter | Description                                                                                                                                                                                                                                                                           |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `-aoa`     | Directly overwrites existing files without any prompts.                                                                                                                                                                                                                             |
| `-aos`     | Skips existing files; they will not be overwritten.                                                                                                                                                                                                                                 |
| `-aou`     | If a file with the same name exists, automatically renames the extracted file. For example, the file `file.txt` will be automatically renamed to `file_1.txt`.                                                                                                                      |
| `-aot`     | If a file with the same name exists, automatically renames the existing file. For example, the file `file.txt` will be automatically renamed to `file_1.txt`.                                                                                                                      |

**Example**

`HaoZipC x test.zip -aoa`: Extract all files from the `test.zip` archive and directly overwrite existing files without prompts.

**Options that can be used with this option:** `e` (extract), `x` (extract with full path).

**Other**

**Options:** `-y` (always).
