# Znaleźć łączną długość wyrazów w stringu line. Wskazówka: można skorzystać z funkcji sum().

def dlugosc_wyrazow(line):
    line = line.split()
    length = 0
    for word in line:
        length += len(word)
    print("Dlugosc napisu ", line, length)
    return length

line1 = "Nie taki diabel straszny jak go maluja"
line2 = "Jak sie czlowiek spieszy to sie diabel cieszy"

assert dlugosc_wyrazow(line1) == 32
assert dlugosc_wyrazow(line2) == 38