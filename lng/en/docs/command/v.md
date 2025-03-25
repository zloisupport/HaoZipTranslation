**Option -v (Create Split Volumes)**

--------------------------------------------------------------------------------

Specifies the volume size.

**Syntax**

`-v{Size}[b | k | m | g]`: `{Size}[b | k | m | g]` specifies the volume size. You can use bytes, KB (1 KB = 1024 bytes), MB (1 MB = 1024 KB), or GB (1 GB = 1024 MB). If you only specify `{Size}`, 2345 HaoZip will treat it as bytes. You can specify several `-v` options simultaneously.

**Example**

`HaoZipC a a.7z *.txt -v10k -v15k -v2m`: Create a split volume for the `a.7z` archive. The first volume is 10 KB, the second is 15 KB, and the rest are 2 MB.

**Command that can be used with this option:** `a` (add).
