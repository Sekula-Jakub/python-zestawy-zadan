# Znaleźć liczbę cyfr zero w dużej liczbie całkowitej. Wskazówka: zamienić liczbę na string.

def ile_zer(liczba):
    string = str(liczba)
    liczba_zer = 0
    for char in string:
        if char == "0":
            liczba_zer = liczba_zer + 1

    print("liczba_zer", liczba_zer)
    return liczba_zer

liczba1 = 1230450
liczba2 = 2124445

assert ile_zer(liczba1) == 2
assert ile_zer(liczba2) == 0