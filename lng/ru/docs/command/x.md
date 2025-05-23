﻿**Опция -x (исключить файлы)**

--------------------------------------------------------------------------------

Указывает один файл или тип файлов, которые следует исключить из операции. Эта опция может исключать несколько типов одновременно.

**Синтаксис**

`-x[<тип_рекурсии>]<ссылка_на_файл>`

`<тип_рекурсии> ::= r[- | 0]`
`<ссылка_на_файл> ::= @{listfile} | !{маска}`

Более подробную информацию смотрите в опции `-i` (прикрепленные файлы).

**Пример**

`HaoZipC a -tzip archive.zip *.txt -x!temp.*`: Добавить все файлы `*.txt`, кроме файлов `temp.*`, в архив `archive.zip`.

**Команды, с которыми можно использовать эту опцию:** `a` (добавить), `d` (удалить), `e` (извлечь), `l` (список), `t` (тест), `u` (обновить), `x` (извлечь с полным путем).

**Другое**

**Опции:** `-r` (рекурсивно сканировать подкаталоги), `-i` (прикрепленные файлы).
