"""
make_osis.py - converts the Wujek Bible from Wikisource EPUB to OSIS
Copyright (C) 2025-2026 Bartosz Gleń

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import os
import sys
from pathlib import Path

from extract.books import parse_toc
from extract.export import OsisExport
from extract.parse import parse

#
# Set working directory to $(BIBLE_DIR)/OPS
#
directory = Path(sys.argv[1]) / "OPS"
cwd = Path.cwd()
os.chdir(directory)

#
# List books
#
toc = parse("toc.ncx")
books = parse_toc(toc)

#
# Extract chapters and verses
#
for book in books:
    book.parse()

    # one chapter for now
    for chapter in book.chapters:
        print(f"[PROCESSING] {book.name} - Chapter {chapter.number}")
        chapter.parse()

#
# OSIS export
#
export = OsisExport()
result = export.export(books)

with open(cwd / "out" / "bwujka.xml", mode="w", encoding="UTF-8") as f:
    f.write(result)
