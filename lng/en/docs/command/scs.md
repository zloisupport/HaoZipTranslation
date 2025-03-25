**Option -scs (Set File List Encoding)**

--------------------------------------------------------------------------------

Sets the encoding of the file list.

**Syntax**

`-scs{UTF-8 | WIN | DOS}`: The default encoding is UTF-8.

* `UTF-8`: Unicode UTF-8.
* `WIN`: Default Windows encoding.
* `DOS`: Default Windows DOS (OEM) encoding.

**Example**

`HaoZipC a archive.7z @listfile.txt -scsWIN`: Archive files from the list `listfile.txt`, which uses the default Windows encoding.

**Commands that can be used with this option**: `a` (add), `u` (update).
