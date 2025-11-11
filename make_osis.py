import os
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

from extract.books import parse_toc
from extract.export import OsisExport


#
# Set working directory to $(BIBLE_DIR)/OPS
#
directory = Path(sys.argv[1]) / 'OPS'
cwd = Path.cwd()
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
book.parse()

# one chapter for now
chapter = book.chapters[0]
chapter.parse()

#
# OSIS export
#
export = OsisExport()
result = export.export([book])

with open(cwd / 'out' / 'bwujka.xml', mode='w', encoding='UTF-8') as f:
    f.write(result)
