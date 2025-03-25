**Option -ssc (Set Case-Sensitive Mode)**

--------------------------------------------------------------------------------

Sets whether the file system will be case-sensitive.

**Syntax**

`-ssc[-]`

| Option   | Description                                                                                                                                    |
|----------|------------------------------------------------------------------------------------------------------------------------------------------------|
| `-ssc`  | Sets case-sensitive mode. This option is used by default in Posix and Linux systems.                                                    |
| `-ssc-` | Sets case-insensitive mode. This option is used by default in Windows systems.                                                          |

**Example**

`HaoZipC a archive.7z A*.txt -ssc -r`

: Compress all files `A*.txt` from the current directory and its subdirectories, but do not include `a*.txt` files.

**Commands that can be used with this option:** `a` (add), `d` (delete), `e` (extract), `l` (list), `t` (test), `u` (update), `x` (extract with full path).
