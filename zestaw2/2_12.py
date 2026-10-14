# Zbudować string stworzony z pierwszych znaków wyrazów ze stringu line.
# Zbudować napis stworzony z ostatnich znaków wyrazów ze stringu line.

def first_letters(line):
    result = ""
    for item in line.split():
        result += item[0]
    print("Pierwsze litery: ", line, result)
    return result

def last_letters(line):
    result = ""
    for item in line.split():
        result += item[-1]
    print("Ostatnie litery: ", line, result)
    return result

line1 = "Nie taki diabel straszny jak go maluja"
line2 = "Jak sie czlowiek spieszy to sie diabel cieszy"

assert first_letters(line1) == "Ntdsjgm"
assert last_letters(line1) == "eilykoa"
print()
assert first_letters(line2) == "Jscstsdc"
assert last_letters(line2) == "kekyoely"