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

from extract.books import is_valid_title, parse_toc
from extract.parse import parse


class TestBooks(unittest.TestCase):
    def test_is_valid_title(self):
        self.assertFalse(
            is_valid_title("Biblia, to jest księgi Starego i Nowego Testamentu")
        )
        self.assertFalse(is_valid_title("Starego Testamentu"))
        self.assertFalse(is_valid_title("Nowego Testamentu"))
        self.assertTrue(is_valid_title("Genesis, to jest pierwsze"))
        self.assertTrue(is_valid_title("Objawienie św. Jana"))

    def test_parse_toc(self):
        tree = parse("tests/toc.ncx")
        books = parse_toc(tree)

        book_count = 66

        self.assertEqual(book_count, len(books))
        self.assertIn("Genesis", books[0].name)
        self.assertIn("Objawienie", books[book_count - 1].name)
