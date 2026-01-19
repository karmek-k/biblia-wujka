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

import unittest
from datetime import date

from extract.books import Book
from extract.chapters import Chapter
from extract.export import OsisExport


class TestOsisExport(unittest.TestCase):
    def test_template(self):
        today = date(2025, 11, 10)

        result = OsisExport.template("", publication_date=today)

        self.assertTrue("<date>2025-11-10</date>" in result)

    def test_export(self):
        books = [
            Book(
                "Genesis, to jest pierwsze",
                href="tests/c2_Biblia_Wujka__1923__Ksiega_Rodzaju.xhtml",
            )
        ]
        books[0].chapters = [
            Chapter(1, href="tests/c42_Biblia_Wujka__1923__Ksiega_Rodzaju_1.xhtml")
        ]
        export = OsisExport()

        result = export.export(books)
        print(result)

        self.assertTrue("<div type='book' osisID='Gen'>" in result)
        self.assertTrue("<chapter osisID='Gen.1'>" in result)
        self.assertTrue(
            "<title>ROZDZIAŁ I. O świata stworzeniu, rzeczy stworzonych różności, i ozdobie; o stanie człowieka, któremu Bóg poddał wszystko, co stworzył.</title>"
            in result
        )
        self.assertTrue(
            "<verse osisID='Gen.1.1'>Na początku stworzył Bóg niebo i ziemię.</verse>"
            in result
        )
