import unittest
import xml.etree.ElementTree as ET

from extract.books import parse_toc, is_valid_title

class TestBooks(unittest.TestCase):
    def test_is_valid_title(self):
        self.assertFalse(is_valid_title('Biblia, to jest księgi Starego i Nowego Testamentu'))
        self.assertFalse(is_valid_title('Starego Testamentu'))
        self.assertFalse(is_valid_title('Nowego Testamentu'))
        self.assertTrue(is_valid_title('Genesis, to jest pierwsze'))
        self.assertTrue(is_valid_title('Objawienie św. Jana'))


    def test_parse_toc(self):
        tree = ET.parse('tests/toc.ncx')
        books = parse_toc(tree)

        self.assertEqual(66, len(books))
        self.assertIn('Genesis', books[0].name)