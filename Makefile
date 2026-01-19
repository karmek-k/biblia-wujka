SOURCE=resources/Biblia_Wujka.epub
BIBLE_DIR=bible-text
OSIS_RESULT=./out/bwujka.xml

PYTHON=python3

osis: bible-text
	mkdir -p out
	$(PYTHON) make_osis.py $(BIBLE_DIR)

sword: osis
	mkdir -p out/bwujka/mods.d out/bwujka/modules/texts/ztext/bwujka
	osis2mod out/bwujka/modules/texts/ztext/bwujka $(OSIS_RESULT) -z -v Vulg
	cp sword/bwujka.conf out/bwujka/mods.d
	cd out/bwujka && zip -r ../bwujka_sword.zip *

bible-text: $(SOURCE)
	unzip $(SOURCE) -d $(BIBLE_DIR)

test:
	$(PYTHON) -m unittest discover -s extract -p "*_test.py"

.PHONY: test
