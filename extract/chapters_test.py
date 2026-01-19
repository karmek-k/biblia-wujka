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

from extract.chapters import Chapter, parse_chapter_toc
from extract.parse import parse


class TestChapters(unittest.TestCase):
    def test_parse_chapter_toc(self):
        href = "tests/c2_Biblia_Wujka__1923__Ksiega_Rodzaju.xhtml"
        tree = parse(href)
        chapter_count = 50

        chapters = parse_chapter_toc(tree)

        self.assertEqual(chapter_count, len(chapters))
        self.assertTrue(chapters[0].href.startswith("c42"))
        self.assertTrue(chapters[chapter_count - 1].href.startswith("c91"))

    def test_chapter_parse(self):
        chapter = Chapter(
            1, href="tests/c42_Biblia_Wujka__1923__Ksiega_Rodzaju_1.xhtml"
        )

        chapter.parse()

        self.assertTrue("O świata stworzeniu" in chapter.title)
        self.assertTrue("ROZDZIAŁ I." in chapter.title)
        self.assertEqual(31, len(chapter.verses))
