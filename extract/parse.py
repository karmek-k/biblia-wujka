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
