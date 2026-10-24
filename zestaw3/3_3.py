# Wypisać w pętli liczby od 0 do 30 włączne, z wyjątkiem liczb podzielnych przez 3.
# Podać dwa rozwiązania, jedno z pętlą for, drugie z pętlą while.

for i in range(31):
    if i % 3 == 0:
        print (i)

i = 0
while(i <= 30):
    if i % 3 == 0:
        print (i)
    i = i + 1