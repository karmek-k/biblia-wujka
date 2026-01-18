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
