# Napisać program rysujący prostokąt zbudowany z małych kratek. Należy zbudować pełny string, a potem go wypisać.
# Liczby kratek w wierszach (y) i kolumnach (x) mają być zapisane w osobnych zmiennych jako parametry programu.

x = 2
y = 2

string = []

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

draw_plus_line(string, x)
for i in range(y):
    draw_bar_line(string, x)
    draw_plus_line(string, x)

string_output = "".join(string)
print(string_output)