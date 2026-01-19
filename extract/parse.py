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

import xml.etree.ElementTree as ET
from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    XmlTree: TypeAlias = ET.ElementTree[ET.Element]
else:
    XmlTree = ET.ElementTree


def parse(filename: str) -> XmlTree:
    """
    Wrapper around `ET.parse` that ensures `ET.ElementTree[ET.Element]`
    is returned, and not `ET.ElementTree[ET.Element | None]`.
    """
    tree = ET.parse(filename)

    return tree
