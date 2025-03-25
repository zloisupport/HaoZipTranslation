**Option -ai (Include Filenames)**

--------------------------------------------------------------------------------

Specifies the files to be included, including archive names and masks. This option allows you to include several types of files at once.

**Syntax**

`-ai[<recurse_type>]<file_reference>`
`<recurse_type> ::= r[- | 0]`
`<file_reference> ::= @{listfile} | !{wildcard}`

**Parameters**

* `<recurse_type>`
* `<file_ref>`: Specifies the filename, mask, or list of files to process.

`<recurse_type> ::= r[- | 0]`
`<file_ref> ::= @{listfile} | !{wildcard}`

| Option      | Description                                                                  |
|--------------|------------------------------------------------------------------------------|
| `{listfile}` | Specifies the name of the file list. See the description for [File List].   |
| `{wildcard}` | Specifies a mask or filename.                                             |

**Example**

`HaoZipC t -an -air!*.7z`: Checks *.7z archives in the current directory and subdirectories.

**Commands that can be used with this option**: `a` (add), `d` (delete), `e` (extract), `l` (list), `t` (test), `u` (update), `x` (extract with full path).

**Other**

**Options:**

`-ax` (exclude filenames), `-an` (disable filename parsing)
