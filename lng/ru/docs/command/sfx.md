﻿**Опция -sfx (создать самораспаковывающийся файл)**

--------------------------------------------------------------------------------

Создает самораспаковывающийся файл.

**Синтаксис**

`-sfx[{SFX_Module}]`:  `{SFX_Module}` - указывает самораспаковывающийся (SFX) модуль, который будет добавлен к архиву. Однако указанный модуль должен находиться в том же каталоге, что и файл `HaoZipC.exe`. Если `{SFX_Module}` не указан, 2345 HaoZip будет использовать самораспаковывающийся модуль командной строки `7zCon.sfx`.

| `SFX_Module`    | Описание                                          |
|-----------------|---------------------------------------------------|
| `HaoZip7zCon.sfx` | Версия для командной строки (DOS).             |
| `HaoZip7zSetup.sfx` | Версия для установочных дисков Windows.       |
