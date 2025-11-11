SOURCE=resources/Biblia_Wujka.epub
BIBLE_DIR=bible-text

PYTHON=python3

osis: bible-text
	mkdir -p out
	$(PYTHON) make_osis.py $(BIBLE_DIR)

bible-text: $(SOURCE)
	unzip $(SOURCE) -d $(BIBLE_DIR)

test:
	$(PYTHON) -m unittest discover -s extract -p "*_test.py"

.PHONY: test