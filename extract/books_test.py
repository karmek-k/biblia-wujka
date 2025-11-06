import unittest
import xml.etree.ElementTree as ET

from extract.books import parse_toc

class TestBooks(unittest.TestCase):
    def test_parse_toc(self):
        tree = ET.parse('tests/toc.ncx')
        books = parse_toc(tree)

        self.assertEqual(66, len(books))