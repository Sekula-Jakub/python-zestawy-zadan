# Mamy dany string wielowierszowy line. Podać sposób obliczenia liczby wyrazów w stringu.
# Przez wyraz rozumiemy ciąg "czarnych" znaków, oddzielony od innych wyrazów białymi
# znakami (spacja, tabulacja, newline).

def ile_wyrazow(line):
    ilosc_wyrazow = len(line.split())
    print("Ilosc wyrazow w stringu ", line, ":", ilosc_wyrazow)
    return ilosc_wyrazow

line1 = "Nie taki diabeł straszny\njak go malują."
line2 = "Jak się człowiek spieszy\nto się diabeł cieszy."

assert ile_wyrazow(line1) == 7
assert ile_wyrazow(line2) == 8
