import os
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

from extract.books import parse_toc
from extract.chapters import parse_chapter_toc


#
# Set working directory to $(BIBLE_DIR)/OPS
#
directory = Path(sys.argv[1]) / 'OPS'
os.chdir(directory)

#
# List books
#
toc = ET.parse('toc.ncx')
books = parse_toc(toc)

#
# Extract chapters and verses
#

# one book and chapter for now
book = books[0]
book.chapters = parse_chapter_toc(ET.parse(book.href)) 

# one chapter for now
chapter = book.chapters[0]
chapter.parse()
