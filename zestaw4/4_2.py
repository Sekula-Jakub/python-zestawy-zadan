# Rozwiązania zadań 3.5 i 3.6 z poprzedniego zestawu zapisać w postaci funkcji, które zwracają pełny string przez
# return. Funkcje nie powinny pytać użytkownika o dane, tylko korzystać z argumentów.

#3.5 - miarka
def make_ruler(n):
    miarka = []
    liczby = []
    x = n
    ile_kropek = 4

    miarka.append("|")
    liczby.append("0")
    for i in range(x):
        ile_cyfr = len(str(i + 1))
        for j in range(ile_kropek):
            miarka.append(".")
        miarka.append("|")

        ile_spacji = ile_kropek - ile_cyfr + 1
        liczby.append((" " * ile_spacji) + str(i + 1))

    miarka.append("\n")

    podzialka_string = "".join(miarka)

    miarka_string = "".join(liczby)

    return podzialka_string + miarka_string

#3.6 - siatka
def make_grid(rows, cols):
    x = rows
    y = cols

    string = []
    draw_plus_line(string, x)
    for i in range(y):
        draw_bar_line(string, x)
        draw_plus_line(string, x)

    string_output = "".join(string)
    return string_output

def draw_plus_line(string, x):
    string.append("+")
    for i in range(x):
        for j in range(3):
            string.append("-")
        string.append("+")

    string.append("\n")

def draw_bar_line(string, x):
    string.append("|")
    for i in range(x):
        for j in range(3):
            string.append(" ")
        string.append("|")

    string.append("\n")

def test_miarka():
    print("Testy dla miarki: ")
    miarka12 = "|....|....|....|....|....|....|....|....|....|....|....|....|\n0    1    2    3    4    5    6    7    8    9   10   11   12"
    miarka6 = "|....|....|....|....|....|....|\n0    1    2    3    4    5    6"
    assert make_ruler(12) == miarka12
    assert make_ruler(6) == miarka6
    print("OK")


def test_siatka():
    print("testy dla siatki: ")
    siatka2x2 = "+---+---+\n"\
                "|   |   |\n"\
                "+---+---+\n"\
                "|   |   |\n"\
                "+---+---+"
    siatka5x5 = (
        "+---+---+---+---+---+\n"
        "|   |   |   |   |   |\n"
        "+---+---+---+---+---+\n"
        "|   |   |   |   |   |\n"
        "+---+---+---+---+---+\n"
        "|   |   |   |   |   |\n"
        "+---+---+---+---+---+\n"
        "|   |   |   |   |   |\n"
        "+---+---+---+---+---+\n"
        "|   |   |   |   |   |\n"
        "+---+---+---+---+---+"
    )
    assert make_grid(2, 2).strip() == siatka2x2
    assert make_grid(5, 5).strip() == siatka5x5
    print("OK")

test_miarka()
test_siatka()


