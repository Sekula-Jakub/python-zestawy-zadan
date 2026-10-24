# Napisać program rysujący "miarkę" o zadanej długości. Długość miarki (x) ma być zapisana w osobnej zmiennej jako
# parametr programu. Należy prawidłowo obsłużyć liczby składające się z kilku cyfr (ostatnia cyfra liczby ma
# znajdować się pod znakiem kreski pionowej). Należy zbudować pełny string, a potem go wypisać.

miarka = []
liczby = []
x = 12
liczba_cyfr = len(str(x))
ile_kropek = liczba_cyfr + 2

miarka.append("|")
liczby.append("0")
for i in range(x):
    ile_cyfr = len(str(i + 1))
    dodano_liczbe = False
    for j in range(ile_kropek):
        miarka.append(".")
    miarka.append("|")

    ile_spacji = ile_kropek - ile_cyfr + 1
    liczby.append((" " * ile_spacji) + str(i + 1))

miarka_string = "".join(miarka)
print(miarka_string)

liczby_string = "".join(liczby)
print(liczby_string)