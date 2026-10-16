# Posortować wyrazy ze stringu line raz alfabetycznie, a raz pod
# względem długości. Wskazówka: funkcja wbudowana sorted().

def sortowanie(line):
    line_splitted = line.split()
    print("Alfabetycznie: ", sorted(line_splitted))
    print("Wedlug dlugosc: ", sorted(line_splitted, key=len))

line1 = "Nie taki diabeł straszny\njak go malują."
line2 = "Jak się człowiek spieszy\nto się diabeł cieszy."

sortowanie(line1)
sortowanie(line2)