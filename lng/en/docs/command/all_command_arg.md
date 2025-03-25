**Command-Line Options**

--------------------------------------------------------------------------------

**Syntax**

`<option>::= <option_symbol><option_characters>[<option>]`
`<option_symbol> ::= '/' | '-'`

In the command line, a complete option consists of the specified option, a hyphen (-) or a forward slash (/), and the option symbol cannot be abbreviated.

Option names are not case-sensitive. However, some options include parameters that are case-sensitive.

Options can be used anywhere on the command line.

For detailed instructions on using the command line, see the [Syntax] section.

**Key Points on Options**

| Option  | Description                                              |
|---------|----------------------------------------------------------|
| `--`   | Prevent option parsing                                  |
| `-ai`   | Include filenames                                       |
| `-an`   | Disable filename parsing                               |
| `-ao`   | Overwrite mode                                          |
| `-ax`   | Exclude filenames                                       |
| `-i`    | Include filenames                                       |
| `-m`    | Set compression algorithm                              |
| `-o`    | Set output directory                                   |
| `-p`    | Set password                                            |
| `-r`    | Recursively scan subdirectories                       |
| `-sfx`  | Create self-extracting archive                           |
| `-si`   | Read data from StdIn                                  |
| `-so`   | Write data to StdOut                                  |
| `-t`    | Set file type                                         |
| `-u`    | Update options                                          |
| `-v`    | Create split volumes                                     |
| `-w`    | Set working directory                                   |
| `-x`    | Exclude files                                         |
| `-y`    | Always (automatically confirm all requests)            |
