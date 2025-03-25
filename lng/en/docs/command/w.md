**Option -w (Set Working Directory)**

--------------------------------------------------------------------------------

Sets the temporary working directory for file compression. By default, when creating a new archive, 2345 HaoZip temporarily creates the base archive in the current directory. However, by specifying this option, you can set the directory for creating the base archive, that is, the working directory. When compression is complete, it will be renamed to the filename you specified before compression, and then the original archive in the temporary directory will be deleted.

**Syntax**

`-w[{dir_path}]`: `{dir_path}` specifies the target folder. If `<dir_path>` is not specified, 2345 HaoZip will use the default Windows temporary directory.

**Example**

`HaoZipC a -tzip archive.zip *.cpp -wc:\temp`: Add `*.cpp` files to the `archive.zip` archive and create a temporary archive in the `c:\temp` folder.

**Commands that can be used with this option:** `a` (add), `d` (delete), `u` (update).
