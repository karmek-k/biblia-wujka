import xml.etree.ElementTree as ET


class Chapter:
    def __init__(self, number: int, *, href: str):
        self.number = number
        self.href = href
        self.title = None

    def __str__(self) -> str:
        return f'Chapter {self.number}'
    
    def __repr__(self) -> str:
        return f'<Chapter number="{self.number}" href="{self.href}">'
    
    def parse(self) -> None:
        # tree = ET.parse(self.href)
        self.title = ''


def parse_chapter_toc(tree: ET.ElementTree) -> list[Chapter]:
    root = tree.getroot()
    namespace = {'xhtml': 'http://www.w3.org/1999/xhtml'}
    
    anchors = root.findall('.//xhtml:a', namespace)
    
    result = []

    for anchor in anchors:
        # only numeric anchor contents have meaningful hrefs
        if not anchor.text.isnumeric():
            continue
        
        result.append(Chapter(int(anchor.text), href=anchor.attrib['href']))

    return result