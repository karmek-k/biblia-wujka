SOURCE=resources/Biblia_Wujka.epub
BIBLE_DIR=bible-text
OSIS_RESULT=./out/bwujka.xml

PYTHON=python3

osis: bible-text
	mkdir -p out
	$(PYTHON) make_osis.py $(BIBLE_DIR)

sword: osis
	mkdir -p out/bwujka
	osis2mod ./out/bwujka $(OSIS_RESULT) -z -v Vulg
	cp sword/bwujka.conf out/

bible-text: $(SOURCE)
	unzip $(SOURCE) -d $(BIBLE_DIR)

test:
	$(PYTHON) -m unittest discover -s extract -p "*_test.py"

.PHONY: test
