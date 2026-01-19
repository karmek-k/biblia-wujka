# Jakub Wujek Bible (OSIS & SWORD)

![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)
![Python: 3.x](https://img.shields.io/badge/python-3.x-blue.svg)

[🇵🇱 README po polsku](README_PL.md)

A project containing tools to convert the **Jakub Wujek Bible** (based on the 1923 edition available on [Wikisource](https://pl.wikisource.org/wiki/Biblia_Wujka_(1923))) into open biblical standards.

It allows you to generate:
1.  **OSIS XML file** – a universal format for exchanging biblical texts.
2.  **SWORD module** – ready for use in applications such as *Xiphos, And Bible, BibleTime,* or *The Word*.

---

## Requirements

To build the project, you need a Linux environment (or WSL) with the following packages installed:

* `python3` – to run the conversion script.
* `make` – to automate the process.
* `unzip` – to extract source data.
* `zip` – to build the SWORD archive.
* `osis2mod` – tool for compiling the SWORD module.
    * *Debian/Ubuntu:* `libsword-utils` or `xiphos` package.
    * *Fedora/RHEL:* `sword-utils` package.

## Building

### Generating the OSIS file
If you only need the XML file (e.g., for further processing):

```bash
make
```

### Generating the SWORD module

To build a ready-to-use, compressed binary module:

```bash
make sword
```

*This process automatically downloads the data, converts it using the `make_osis.py` script, and compiles it using `osis2mod`.*

---

## Technical Details

The `make_osis.py` script is responsible for fetching EPUB content from Wikisource, cleaning it, and formatting it to the OSIS standard, taking into account the specifics of the Polish text of the Wujek Bible.

### Copyright

The original text of the Bible (translated by Fr. Jakub Wujek) is in the **public domain**.

Conversion tools:

> make_osis.py - converts the Wujek Bible from Wikisource EPUB to OSIS
>
> Copyright (C) 2025-2026 Bartosz Gleń
> 
> This program is free software: you can redistribute it and/or modify
> it under the terms of the GNU General Public License as published by
> the Free Software Foundation, either version 3 of the License, or
> (at your option) any later version.
> 
> This program is distributed in the hope that it will be useful,
> but WITHOUT ANY WARRANTY; without even the implied warranty of
> MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
> GNU General Public License for more details.
> 
> You should have received a copy of the GNU General Public License
> along with this program.  If not, see \<https://www.gnu.org/licenses/>.
