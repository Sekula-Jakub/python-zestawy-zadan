x = 2; y = 3;
if (x > y):
    result = x;
else:
    result = y;

# Kod jest poprawny ponieważ zmienna result nie jest ograniczona tylko do bloku else

for i in "axby": if ord(i) < 100: print (i)

# Kod jest niepoprawny - nie można umieszczać w tej samej linii po for instrukcji if

for i in "axby": print (ord(i) if ord(i) < 100 else i)

# Kod jest poprany - instrukcja print jest dozwolona w tej samej lini co pętla for