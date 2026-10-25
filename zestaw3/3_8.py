# Dla dwóch sekwencji liczb lub znaków znaleźć:
# (a) listę elementów występujących jednocześnie w obu sekwencjach (bez powtórzeń),
# (b) listę wszystkich elementów z obu sekwencji (bez powtórzeń).

sek1 = [1, 2, 3, 4, 5, 1 ,2]
sek2 = [6, 7, 8, 0, 1, 7, 1]

def compare(sek1, sek2):
    set1 = set(sek1)
    set2 = set(sek2)

    wspolne = list(set1 & set2)
    wszystkie = list(set2 | set1)

    return wspolne, wszystkie

wspolne, wszystkie = compare(sek1, sek2)

print("(a) Wspólne elementy:", wspolne)
print("(b) Wszystkie elementy:", wszystkie)