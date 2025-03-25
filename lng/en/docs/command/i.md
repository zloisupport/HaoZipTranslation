**Option -i (Include Files)**

--------------------------------------------------------------------------------

Specifies a single file or type of files to include. This option can include multiple types simultaneously.

**Syntax**

`-i[<recurse_type>]<file_reference>`

`<recurse_type> ::= r[- | 0]`
`<file_reference> ::= @{listfile} | !{wildcard}`

**Reference**

* `<recurse_type>`: This value should be used in this option. If the value of this option does not exist, the value specified by the `-r` option (recursively scan subdirectories) will be used. See the `-r` option (recursively scan subdirectories) for more information.
`<recurse_type> ::= r[- | 0]`

* `<file_ref>`: Specify a filename or a mask, or use a file list to add files.
`<file_ref> ::= @{listfile} | !{wildcard}`

| Parameter   | Description                                                        |
|-------------|--------------------------------------------------------------------|
| `{listfile}` | Specifies the list of files. See information related to [File List]. |
| `{wildcard}` | Specifies a filename or mask.                                   |

**Example**

`HaoZipC a -tzip src.zip *.txt -ir!DIR1\*.cpp`: Add `*.txt` files from the current directory and `*.cpp` files from the `DIR1` directory and its subdirectories to the `src.zip` archive.

**Commands that can be used with this option:** `a` (add), `d` (delete), `e` (extract), `l` (list), `t` (test), `u` (update), `x` (extract with full path).

**Other**

**Options:** `r` (recursively scan subdirectories), `-x` (exclude files)
