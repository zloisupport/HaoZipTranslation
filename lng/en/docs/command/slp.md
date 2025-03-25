**Option -slp (Set Large Pages Mode)**

--------------------------------------------------------------------------------

Sets the large pages mode.

**Syntax**

`-slp[-]`

| Option  | Description                                                                                                                                                                                                                                                                                                                                                      |
|---------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `-slp` | Enable large pages mode.                                                                                                                                                                                                                                                                                                                                |
| `-slp-`| Disable large pages mode. This is the default value.                                                                                                                                                                                                                                                                                                |

If this feature is enabled, 2345 HaoZip will attempt to use large memory pages. This feature may speed up compression. However, HaoZip will have to allocate large memory pages at the beginning of compression, which will cause some delays. In addition, if HaoZip uses large memory pages, the task manager will not display the actual value of memory used by the program. This feature can only work in Windows 2003 / XP x64 / Vista. And you must have system administrator rights. Recommended memory: 1 GB or more. To properly configure this feature, you must run the HaoZip file manager at least once, close it, and restart the system.

**Example**

`HaoZipC a archive.7z -slp a.iso`: Compress the file `a.iso` in large pages mode.
