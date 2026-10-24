L = [3, 5, 4] ; L = L.sort()
# L.sort() sortuje liste w miejcu więc do zmiennej L przypisze się None

x, y = 1, 2, 3
# inny liczba zmiennych i wartości

X = 1, 2, 3 ; X[1] = 4
# X będzie krotką, która jest niemutowalna.

X = [1, 2, 3] ; X[3] = 4
# Wystąpi błąd index out of bounds

X = "abc" ; X.append("d")
# X jest stringiem, czyli jest niemutowalny. Nie można na nim wywoływać append()\

L = list(map(pow, range(8)))
# funkcja pow() wymaga dwóch argumentów: podsatwy oraz wykładnika potęgi