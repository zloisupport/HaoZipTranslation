**Option -si (Read Data from stdin)**

--------------------------------------------------------------------------------

Allows HaoZip to use data from stdin (standard input stream).

**Syntax**

`-si{file_name}`: `{file_name}` - specifies the name for the data that will be saved in the archive. If `file_name` is not specified, the data will be saved without a name. Warning: the current version of 2345 HaoZip does not support reading archives from stdin.

**Example**

`HaoZipC a archive.gz -tgzip -siDoc2.txt < Doc.txt`: Compress the input stream from the file `Doc.txt` with the filename `Doc2.txt` into the `archive.gz` archive.

**Commands that can be used with this option:** `a` (add), `u` (update)
