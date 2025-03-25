**Option -an (Disable Filename Parsing)**

--------------------------------------------------------------------------------

Do not parse the `archive_name` area in the command line. This option should be used together with the `-i` option (include files). For example, if you use a file list for archives, you need to specify the `-ai` option, so you need to disable parsing of the `archive_name` area in the command line.

**Syntax**

`-an`

**Example**

`HaoZipC t -an -ai!*.7z -ax!a*.7z`: Checks *.7z archives, except a*.7z.

**Commands that can be used with this option**: `e` (extract), `l` (list), `t` (test), `x` (extract with full path).

**Other**

**Options:**

`-i` (include files), `-x` (exclude files)
