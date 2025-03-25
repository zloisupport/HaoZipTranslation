**Option -u (Update Options)**

--------------------------------------------------------------------------------

Specifies how to update and create files in the archive.

**Syntax**

`-u[-]<action_set>[!{new_archive_name}]`
`<action_set> ::= <state_action>...`
`<state_action> ::= <state><action>`
`<state> ::= p | q | r | x | y | z | w`
`<action> ::= 0 | 1 | 2 | 3`

**Reference**

Hyphen (-): Do not perform any updates to the source archive.

`{new_archive_name}`: Specifies the path to the new archive.

`<state>`: `<state> ::= p | q | r | x | y | z | w`, each filename will be assigned the following six variables:

| `<state>` | Description                                                                                              | File on disk         | File in archive         |
|-----------|----------------------------------------------------------------------------------------------------------|---------------------|---------------------|
| `p`       | The file is in the archive but does not match the file on disk.                                            | Exists, does not match | Exists, does not match |
| `q`       | The file is in the archive but is missing on disk.                                                       | Missing             | Exists              |
| `r`       | The file is missing from the archive but exists on disk.                                                  | Exists              | Missing             |
| `x`       | The file in the archive is newer than the file on disk.                                                     | Older               | Newer              |
| `y`       | The file in the archive is older than the file on disk.                                                     | Newer               | Older              |
| `z`       | The file in the archive and the file on disk are identical.                                               | Identical           | Identical           |
| `w`       | Cannot determine whether the file is newer (same time but different size).                               | ?                   | ?                   |

`<action>`: Specifies the action for the corresponding `<state>`. `<action> ::= 0 | 1 | 2 | 3`, you can specify any of the following four action variables:

| `<action>` | Description                                                                                                                                                                                                                                                 |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `0`       | Ignore the file (do not create an element for this file in the archive).                                                                                                                                                                                 |
| `1`       | Copy the file (overwrite the old file with the new file from the archive).                                                                                                                                                                                  |
| `2`       | Archive the file (archive the new file from disk to the archive).                                                                                                                                                                                               |
| `3`       | Create an element for exclusion (delete the file or directory element during the extraction process). This feature is only supported for the 7z format.                                                                                                |

Attention: Any update command (for example, `a` (add), `d` (delete), `u` (update)) can be assigned to the following elements. The following table shows the action settings for the update commands:

| Command \\ `<state>` | `p` | `q` | `r` | `x` | `y` | `z` | `w` |
|--------------------------|-----|-----|-----|-----|-----|-----|-----|
| `d` (delete)             | `1` | `0` | `0` | `0` | `0` | `0` | `0` |
| `a` (add)                | `1` | `1` | `2` | `2` | `2` | `2` | `2` |
| `u` (update)             | `1` | `1` | `2` | `1` | `2` | `1` | `2` |

This option can update multiple files at the same time. 2345 HaoZip can create any number of new archives in a single operation.

**Example**

`HaoZipC u c:\1\exist.7z -u- -up0q3x2z0!c:\1\update.7z * -r`: Create a new archive `update.7z` and write to it all the different files from the archive `exist.7z`, located in the current directory. Do not modify the contents of the `exist.7z` archive.

**Commands that can be used with this option:** `a` (add), `d` (delete), `u` (update).
