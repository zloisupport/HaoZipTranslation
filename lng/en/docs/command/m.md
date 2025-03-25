**Option -m (Set Compression Algorithm)**

--------------------------------------------------------------------------------

Specifies the compression algorithm.

**Syntax**

`-m<method_parameters>`: The format of this option depends on the archive type.

**Zip**

| Parameter        | Default Value | Description                                                                     |
|----------------|---------------|-------------------------------------------------------------------------------|
| `x=[0 | 5 | 9]`  | `5`           | Sets the compression level.                                                 |
| `m={MethodID}`   | `Deflate`     | Sets the compression algorithm: `Copy`, `Deflate`, `Deflate64`, `BZip2`.   |
| `fb={NumFastBytes}`| `32`          | Sets the word size for the Deflate encoder.                                 |
| `pass={NumPasses}`| `1`           | Sets the number of passes for the Deflate encoder.                             |

`x=[0 | 5 | 9]`

Sets the compression level:

| Compression Level | Description                                                                  |
|-----------------|-----------------------------------------------------------------------------|
| `0`              | Do not compress.                                                              |
| `5`              | Default compression level.                                                      |
| `9`              | Maximum compression level. Compressed files will be smaller, but compression will be slower and require more RAM. |

`fb={NumFastBytes}`: Sets the word size for the Deflate encoder. You can change it in the range from 3 to 255. Its default value is 32 for the Deflate algorithm and 64 for the Deflate64 algorithm. If several compressible files have many identically located bytes, for example, two plain text documents with very similar content and format, then compression with a larger word size will to some extent increase the compression ratio. Therefore, as a rule, the larger this value, the smaller the compressed file will be. But compression and decompression will be slower and require more RAM.

`pass={NumPasses}`: Sets the number of passes for the Deflate encoder. You can change it in the range from 1 to 4. Its default value is 1 for the Deflate algorithm and 3 for the Deflate64 algorithm. This parameter can slightly improve the compression ratio, but not significantly.

**GZip**

GZip uses the same parameters as Zip, except that GZip does not support the "Store" compression algorithm.

**7z**

| Parameter       | Default Value | Description                                                                                                                              |
|----------------|---------------|----------------------------------------------------------------------------------------------------------------------------------------|
| `x=[0 | 1 | 5 | 7 | 9]` | `5`           | Sets the compression level.                                                                                                |
| `s=[off | on | [e] [{N}f] [{N}b | {N}k | {N}m | {N}g]]` | `on`          | Sets the solid mode.                                                                                             |
| `f=[off | on]`  | `on`          | Enables or disables the executable file compression filter.                                                                                          |
| `hc=[off | on]` | `on`          | Enables or disables file header compression.                                                                                        |
| `hcf=[off | on]`| `on`          | Enables or disables full file header compression.                                                                                   |
| `he=[off | on]` | `off`         | Enables or disables file header encryption.                                                                                     |
| `b{C1}[s{S1}]:{C2}[s{S2}]` |               | Sets linking between encoders.                                                                                             |
| `{N}={MethodID}[:param1][:param2][..]` | `LZMA`      | Sets the compression algorithm: `LZMA`, `PPMd`, `BZip2`, `Deflate`, `BCJ`, `BCJ2`, `Copy`.                                      |
| `mt=[off | on]` | `off`         | Sets the multithreaded mode.                                                                                             |

`x=[0 | 1 | 5 | 7 | 9]`

Sets the compression level:

| Compression Level | Description                                                                                                          |
|-----------------|----------------------------------------------------------------------------------------------------------------------|
| `0`              | Do not compress.                                                                                                        |
| `1`              | Fast compression: fast LZMA algorithm, dictionary size 32 KB, match finder HC3, BCJ filter.                        |
| `5`              | Normal compression: standard LZMA algorithm, dictionary size 2 MB, match finder BT4, word size 32, BCJ filter.    |
| `7`              | Maximum compression: maximum LZMA algorithm, dictionary size 8 MB, match finder BT4, word size 64, BCJ filter.     |
| `9`              | Extreme compression: maximum LZMA algorithm, dictionary size 32 MB, match finder BT4b, word size 64, BCJ2 filter. |

`s=[off | on | [e] [{N}f] [{N}b | {N}k | {N}m | {N}g]]`: Enables or disables solid mode. The default value for this option is `s=on`. In solid compression mode, all files in the archive are treated as a continuous data stream. As a rule, solid compression can increase the compression ratio, especially when adding a large number of small files.
* `e` Uses separate solid data streams for each file extension
* `{N}f` Sets the number of files in one solid data stream
* `{N}b | {N}k | {N}m | {N}g` Sets the size of the solid data stream (in bytes)
Different compression levels have restrictions on the size of the solid data stream:

| Compression Level | Size       |
|-----------------|------------|
| Store           | 0 B        |
| Fast            | 16 MB      |
| Normal          | 256 MB     |
| Maximum         | 1 GB       |
| Extreme         | 4 GB       |
Restrictions on the size of the solid data stream, although they affect the compression ratio, have a number of advantages: in case of archive corruption, not all data will be lost; the time for extracting files is reduced.

In the current version, you can only update archives that were not compressed with solid mode enabled. That is, the current version does not support updating archives with solid mode.

Example: `-s=100f10m`: Set solid mode so that each solid data stream contains no more than 100 files and has a maximum size of 10 MB.

`f=[off | on]`: Enables or disables the executable file compression filter: dll, exe, ocx, sfx, sys. It is used in the BCJ2 filter (using extreme compression) and the BCJ filter. The default value for this option is `f=on`.

`hc=[off | on]`: Enables or disables file header compression. The default value for this option is `hc=on`. If file header compression is enabled, part of the file headers will be compressed using the LZMA algorithm.

`hcf=[off | on]`: Enables or disables full file header compression. The default value for this option is `hcf=on`. If full file header compression is enabled, this archive will only be supported by HaoZip 2.30 beta 25 and above.

`he=[off | on]`: Enables or disables file header encryption. The default value for this option is `he=off`.

`{N}`: Sets the order of algorithms. It is used as an algorithm binding parameter. The minimum value is 0. The algorithm with the comma will be used first.

`b{C1}[s{S1}]:{C2}[s{S2}]`: Links the output stream S1, encoded by encoder C1, to the input stream S2, encoded by encoder C2. If the data stream number is not specified, the default data stream is S0. As a rule, the encoder has one input and one output stream. But in 2345 HaoZip, some encoders have multiple input and output streams. For example, the BCJ2 encoder has one input and four output streams.

`mt=[off | on]`: Enables or disables multithreaded compression. In multithreaded support mode, 2345 HaoZip will use two threads for compression. Thus, for multiprocessor systems, the compression speed will increase by 70-80%. For Pentium 4 processors with Hyper-Threading, the compression speed will increase by about 25%. But when unpacking, only one thread is used. Warning! This option is only valid for the LZMA compression algorithm.

`{N}={MethodID}[:param1][:param2] ... [:paramN]`: Sets the compression algorithm. In the 7z format, you can use many compression algorithms. The default algorithm for this option is LZMA. This parameter must be one of the following formats: `{ParamName}={ParamValue}`; `{ParamName}{ParamValue}`, where `{ParamValue}` is a numerical value, and `{ParamName}` does not contain digits.

Supported compression algorithms:

| MethodID  | Description                                                                                                                                                                                                                                           |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `LZMA`    | Compression algorithm based on LZ (Lempel-Ziv) co-developed by Israeli mathematicians A.Lempel and J.Ziv. It provides relatively fast decompression speeds (approximately 10-20 times faster than compression). Memory requirements also vary (see the d={Size}[b|k|m] option for more information). |
| `PPMd`    | PPM-based compression algorithm. It is based on Dmitry Shkarin's PPMdH algorithm and optimized for his source code. Usually provides high compression ratio and fast decompression speed of plain text.                                               |
| `BZip2`   | Standard BWT-based compression algorithm. Usually provides a high compression ratio for plain text and fairly good decompression speed.                                                                                                              |
| `Deflate` | Standard compression algorithm for ZIP and GZip formats. Does not have a high compression ratio. But it has a very fast compression and decompression speed. The Deflate compression algorithm only supports a dictionary size of 32 KB.                                |
| `BCJ`     | (CALL, JUMP) 32-bit x86 executable file converter.                                                                                                                                                                                                 |
| `BCJ2`    | (CALL, JUMP, JCC) 32-bit x86 executable file converter (second version).                                                                                                                                                                              |
| `Copy`    | Do not compress.                                                                                                                                                                                                                                      |

**LZMA**

LZMA is a compression algorithm based on Lempel-Ziv (a compression algorithm co-developed by Israeli mathematicians A.Lempel and J.Ziv). It can provide a relatively fast decompression speed (approximately 10-20 times faster than compression). Memory requirements also vary (see the d={Size}[b|k|m] option for more information).

| Parameter        | Default Value | Description                                                                                                                                                                                          |
|----------------|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `a=[0|1|2]`    | `1`           | Sets the compression level: 0 = fast, 1 = normal, 2 = maximum. The default value is 1.                                                                                                                     |
| `d={Size}[b|k|m]` | `20`          | Sets the dictionary size for the LZMA compression algorithm. You can specify this value in bytes, KB or MB. The maximum dictionary size is 256 MB = 2^28 bytes. The default LZMA dictionary size in normal mode is 21 (2 MB); in maximum mode (-mx=7) - 23 (8 MB); in extreme mode (-mx=9) - 25 (32 MB). Unpacking files compressed with the LZMA algorithm requires 64 MB of available physical memory if the dictionary size of the compressed file is 64 MB. |
| `mf={MF_ID}`   | `bt4`         | Sets the matcher for the LZMA compression algorithm. The default algorithm is bt4. bt* algorithms require less memory than pat* algorithms. As a rule, bt4 works much faster than pat*, but some file formats may work quickly with the pat* algorithm. hc* algorithms do not have a good compression ratio, but usually work quite quickly when used in combination with the fast mode (a=0). The required memory depends on the dictionary size (see the table below). |
| `fb={N}`      | `32`          | Sets the word size for the LZMA compression algorithm. The valid range is from 5 to 273. The default value is 32 in normal mode and 64 in maximum mode. As a rule, a larger value can slightly improve the compression ratio. But this will also slow down the compression speed. |
| `lc={N}`      | `3`           | Sets the number of literal context bits. The valid range is from 0 to 8. The default value is 3. Sometimes lc=4 is automatically used for files with large files. |
| `lp={N}`      | `0`           | Sets the number of literal position bits. The valid range is from 0 to 4. The default value is 0.                                                                                               |
| `pb={N}`      | `2`           | Sets the number of position bits. The valid range is from 0 to 4. The default value is 2.                                                                                                      |

**PPMd**

PPMd is short for PPM-based compression algorithm. It is based on Dmitry Shkarin's PPMdH algorithm and optimized for his source code. PPMd usually provides a high compression ratio for plain text and fast decompression speed. Compression and decompression speeds are exactly the same, as is the required amount of memory.

| Parameter        | Default Value | Description                                                                                                                                                                                                 |
|----------------|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `mem={Size}[b|k|m]` | `24`          | Sets the amount of memory used by the PPMd algorithm. You can specify this value in bytes, KB or MB. The maximum value is 2 GB = 2^31 bytes; The default value is 24 (16 MB). If you do not specify the [b|k|m] element, the dictionary size will be automatically selected according to the compression level. PPMd requires the same amount of memory during compression and decompression. |
| `o={Size}`      | `6`           | Sets the compression order for the PPMd algorithm. Its size should be in the range [2,32]. The default value is 6.                                                                                              |

**BCJ2**

BCJ2 is a 32-bit x86 executable file converter (second version). It further compresses files by transforming branch instructions.

The BCJ2 encoder has one input stream and four output streams:

* `s0`: Main stream. Requires further compression.
* `s1`: CALL value transformation stream. Requires further compression.
* `s2`: JUMP value transformation stream. Requires further compression.
* `s3`: Service stream. Already compressed.

When using the LZMA compression algorithm, the dictionary sizes of the streams `s1` and `s2` can be much smaller than that of the stream `s0` (in most cases 512 KB is sufficient).

**Examples**

* `HaoZipC a -tzip archive.zip *.jpg -mx0`: Add `*.jpg` files to the `archive.zip` archive without compression.
* `HaoZipC a -t7z archive.7z *.exe *.dll -m0=BCJ -m1=LZMA:d=21 -ms -mmt`: Add `*.exe` and `*.dll` files to the solid archive `archive.7z`. Use the LZMA compression algorithm, dictionary size 2 MB and BCJ converter. Enable multithreaded optimization (if available).
* `HaoZipC a -t7z archive.7z *.exe *.dll -m0=BCJ2 -m1=LZMA:d23 -m2=LZMA:d19 -m3=LZMA:d19 -mb0:1 -mb0s1:2 -mb0s2:3`: Add `*.exe` and `*.dll` files to the `archive.7z` archive using the BCJ2 converter. The main output stream (s0) uses the LZMA compression algorithm with a dictionary size of 8 MB, and the output streams s1 and s2 of the BCJ2 converter use the LZMA compression algorithm with a dictionary size of 512 KB.
* `HaoZipC a -t7z archive.7z *.txt -m0=PPMd`: Add `*.txt` files to the `archive.7z` archive. Use the PPMd compression algorithm.

**Commands that can be used with this option:** `a` (add), `d` (delete), `u` (update).

**Other options:** `-t` (set archive format).
