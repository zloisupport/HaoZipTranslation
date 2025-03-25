**Option -sfx (Create Self-Extracting Archive)**

--------------------------------------------------------------------------------

Creates a self-extracting archive.

**Syntax**

`-sfx[{SFX_Module}]`: `{SFX_Module}` specifies the self-extracting (SFX) module that will be added to the archive. However, the specified module must be in the same directory as the `HaoZipC.exe` file. If `{SFX_Module}` is not specified, 2345 HaoZip will use the command line self-extracting module `7zCon.sfx`.

| `SFX_Module`      | Description                                         |
|--------------------|-----------------------------------------------------|
| `HaoZip7zCon.sfx`  | Command line (DOS) version.                        |
| `HaoZip7zSetup.sfx` | Windows setup disk version.                        |
