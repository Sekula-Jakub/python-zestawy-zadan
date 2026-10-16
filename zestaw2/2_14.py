# Znaleźć: (a) najdłuższy wyraz, (b) długość najdłuższego wyrazu w stringu line.

def najdluzszy_wyraz(line):
    line_splitted = line.split()
    max_size = len(line_splitted[0])
    max_word = line_splitted[0]
    for item in line_splitted:
        if(len(item) > max_size):
            max_size = len(item)
            max_word = item
    print("Najdluzsze slowo w ", line, " to ", max_word, " dlugosc: ", max_size)
    return max_word

line1 = "Nie taki diabel straszny jak go maluja"
line2 = "Jak sie czlowiek spieszy to sie diabel cieszy"

assert najdluzszy_wyraz(line1) == "straszny"
assert najdluzszy_wyraz(line2) == "czlowiek"