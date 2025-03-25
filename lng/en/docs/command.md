**Basic Commands**

--------------------------------------------------------------------------------

`HaoZipC <command> [<option>...] <base_archive_name> [<parameters>...]`

`<parameters> ::= <option> | <mask> | <filename> | <file_list>`
`<option>::= <option_symbol><option_characters>[<option>]`
`<option_symbol> ::= '/' | '-'`
`<file_list> ::= @{filename}`

Expressions in square brackets ("[" and "]") are optional.

Expressions in angle brackets ("<" and ">") are expressions that need to be replaced (removing the brackets).

Expression:

`expression1 | expression2 | ... | expressionN`

The command and options can use both uppercase and lowercase letters.

The first command must be a parameter without options.

The order of entering options and other filenames can be arbitrary.

Masks or filenames containing spaces must be enclosed in quotes:

`"Dir\Program files\*"`

A mask is a keyboard character, such as an asterisk (*) or a question mark (?), that can be used to represent one or more characters when performing file addition, file extraction, file selection, file deletion, etc. Masks are often used to replace one or more characters when you don't know the actual characters or don't want to type the full name.

Masks similar to Windows are supported:

`"*"` An asterisk can be used to replace zero or more characters.
`"?"` A question mark can be used to replace one character in a name.

A non-standard method of processing masks is used by the operating system, so 2345 HaoZip does not support other rules for masks. In the system `*.*` corresponds to all files. And 2345 HaoZip will consider this as all files with any extension. Therefore, to process all files, you must use the mask `*`.

Examples:

```
*.txt
```

This will find (add, select...) all files with the ".txt" extension.

```
?a*
```

This will find (add, select...) all files where the second letter is "a".

```
*1*
```

This will find (add, select...) all files containing "1".

```
*.*.*
```

This will find (add, select...) all files with a double extension containing ".".

If there is no filename in the command line, the system will use the default mask "*".

Restrictions on the use of masks and filenames in files:

Masks and filenames must not include a system drive letter or URL. Each path to a mask and filename will be treated as a full path from the drive letter to the current directory / a full path starting from the archive root directory. In other words, the initial part of the path (the characters before the first forward slash ("\")) must be some name or mask.
Masks and filenames must not end with a forward slash ("\").
Masks can only appear in the last part of the full path.

Examples:

```
Dir1\*.cpp
```
Correct

```
c:\Dir1\*.cpp
```
Error: the path must not include a drive letter

```
Dir1\Dir2\g?.txt
```
Correct

```
Dir1\D?r2\file1.txt
```
Error: masks can only be used in the last part of the path

**File List**

You can use a file list to batch process files. Filenames in the file must be separated by spaces or a newline. (If spaces are used, each file must be enclosed in quotes).

The command line supports working with multiple file lists simultaneously.

For example, there is a file list "listfile.txt" containing the following:

`"My programs\*.cpp" Src\*.cpp`

Then you can enter the command:

`HaoZipC a -tzip archive.zip @listfile.txt`

This will add all files with the "cpp" extension from the "My programs" and "Src" directories to the "archive.zip" archive.
