# Stworzyć słownik tłumaczący liczby zapisane w systemie rzymskim (z literami I, V, X, L, C, D, M jako stringami)
# na liczby arabskie (podać kilka sposobów tworzenia takiego słownika). Mile widziany kod tłumaczący całą liczbę
# '[funkcja roman2int()].

def roman2int(string):
    rzymskie = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    wynik = 0
    poprzednia_wartosc = 0

    for znak in reversed(string.upper()):
        wartosc = rzymskie[znak]

        if wartosc < poprzednia_wartosc:
            wynik -= wartosc
        else:
            wynik += wartosc

        poprzednia_wartosc = wartosc

    return wynik

print(roman2int("MCMXCIV"))