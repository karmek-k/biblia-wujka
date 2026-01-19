# Biblia Jakuba Wujka (OSIS & SWORD)

![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)
![Python: 3.x](https://img.shields.io/badge/python-3.x-blue.svg)

Projekt zawierający narzędzia do konwersji **Biblii Jakuba Wujka** (na podstawie wydania z 1923 r. dostępnego w [Wikiźródłach](https://pl.wikisource.org/wiki/Biblia_Wujka_(1923))) do otwartych standardów biblijnych.

Pozwala wygenerować:
1.  **Plik OSIS XML** – uniwersalny format wymiany tekstów biblijnych.
2.  **Moduł SWORD** – gotowy do użycia w aplikacjach takich jak *Xiphos, And Bible, BibleTime* czy *The Word*.

---

## Wymagania

Aby zbudować projekt, potrzebujesz środowiska Linux (lub WSL) z zainstalowanymi poniższymi pakietami:

* `python3` – do uruchomienia skryptu konwertującego.
* `make` – do automatyzacji procesu.
* `unzip` – do rozpakowania danych źródłowych.
* `osis2mod` – narzędzie do kompilacji modułu SWORD.
    * *Debian/Ubuntu:* pakiet `libsword-utils` lub `xiphos`.
    * *Fedora/RHEL:* pakiet `sword-utils`.

## Budowanie

### Generowanie pliku OSIS
Jeśli potrzebujesz tylko pliku XML (np. do dalszej obróbki):

```bash
make
```

### Generowanie modułu SWORD

Aby zbudować gotowy, skompresowany moduł binarny:

```bash
make sword
```

*Proces ten automatycznie pobierze dane, przekonwertuje je skryptem `make_osis.py` i skompiluje przy użyciu `osis2mod`.*

---

## Szczegóły techniczne

Skrypt `make_osis.py` odpowiada za pobranie treści EPUB z Wikiźródeł, oczyszczenie jej i sformatowanie do standardu OSIS, uwzględniając specyfikę polskiego tekstu Biblii Wujka.

### Prawa autorskie

Oryginalny tekst Biblii (przekład ks. Jakuba Wujka) znajduje się w **domenie publicznej**.

Narzędzia konwertujące:

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
