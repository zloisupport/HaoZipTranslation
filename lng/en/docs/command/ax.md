**Option -ax (Exclude Filenames)**

--------------------------------------------------------------------------------

Specifies the archives to be excluded from the operation. This option allows you to exclude several types of files at once.

**Syntax**

`-ax[<recurse_type>]<file_reference>`
`<recurse_type> ::= r[- | 0]`
`<file_reference> ::= @{wildcard} | !{mask}`: For detailed information on the parameters of this option, see the -i option (add files).

**Example**

`HaoZipC t -an -ai!*.7z -ax!a*.7z`: Checks *.7z archives, except a*.7z.

**Commands that can be used with this option**: `e` (extract), `l` (list), `t` (test), `x` (extract with full path).

**Other**

**Options:**

`i` (add files), `-an` (disable filename parsing)
