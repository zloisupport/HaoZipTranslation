**Option -x (Exclude Files)**

--------------------------------------------------------------------------------

Specifies a single file or type of files to exclude from the operation. This option can exclude multiple types at once.

**Syntax**

`-x[<recurse_type>]<file_reference>`

`<recurse_type> ::= r[- | 0]`
`<file_reference> ::= @{listfile} | !{wildcard}`

See the `-i` option (include files) for more information.

**Example**

`HaoZipC a -tzip archive.zip *.txt -x!temp.*`: Add all `*.txt` files, except `temp.*` files, to the `archive.zip` archive.

**Commands that can be used with this option:** `a` (add), `d` (delete), `e` (extract), `l` (list), `t` (test), `u` (update), `x` (extract with full path).

**Other**

**Options:** `-r` (recursively scan subdirectories), `-i` (include files).
