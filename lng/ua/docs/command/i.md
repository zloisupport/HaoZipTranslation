﻿

**Опция -i (прикрепленные файлы)**

--------------------------------------------------------------------------------

Указывает один прикрепляемый файл или тип файлов. Эта опция может прикреплять несколько типов одновременно.

**Синтаксис**

`-i[<тип_рекурсии>]<ссылка_на_файл>`

`<тип_рекурсии> ::= r[- | 0]`
`<ссылка_на_файл> ::= @{listfile} | !{маска}`

**Справочник**

* `<recurse_type>`: Это значение должно быть использовано в этой опции. Если значение этой опции не существует, то будет использовано значение, указанное опцией `-r` (рекурсивно сканировать подкаталоги). Дополнительную информацию см. в опции `-r` (рекурсивно сканировать подкаталоги).
`<recurse_type> ::= r[- | 0]`

* `<file_ref>`: Укажите имя файла или маску, или используйте список файлов для добавления файлов.
`<file_ref> ::= @{listfile} | !{маска}`

| Параметр    | Описание                                                        |
|------------|-----------------------------------------------------------------|
| `{listfile}` | Указывает список файлов. См. информацию, связанную со [Списком файлов]. |
| `{wildcard}` | Указывает имя файла или маску.                                |

**Пример**

`HaoZipC a -tzip src.zip *.txt -ir!DIR1\*.cpp`: Добавить файлы `*.txt` из текущего каталога и файлы `*.cpp` из каталога `DIR1` и его подкаталогов в архив `src.zip`.

**Команды, с которыми можно использовать эту опцию:** `a` (добавить), `d` (удалить), `e` (извлечь), `l` (список), `t` (тест), `u` (обновить), `x` (извлечь с полным путем).

**Другое**

**Опции:** `r` (рекурсивно сканировать подкаталоги), `-x` (исключить файлы)
