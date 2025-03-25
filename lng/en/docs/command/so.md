**Option -so (Write Data to stdout)**

--------------------------------------------------------------------------------

Allows HaoZip to use data from stdout (standard output stream).

**Syntax**

`-so`

**Examples**

`HaoZipC x archive.gz -so > Doc.txt`: Unpack the output stream from `archive.gz` and write that stream to the file `Doc.txt`.

`HaoZipC a dummy -tgzip -so Doc.txt > archive.gz`: Compress the output stream from `Doc.txt` and write that stream to the archive `archive.gz`.

**Commands that can be used with this option:** `a` (add), `e` (extract), `u` (update), `x` (extract with full path)
