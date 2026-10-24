# Napisać program pobierający w pętli od użytkownika liczbę rzeczywistą x (typ float) i wypisujący x oraz trzecią
# potęgę x. Zatrzymanie programu następuje po wpisaniu z klawiatury stop. Jeżeli użytkownik wpisze napis zamiast
# liczby, to program ma wypisać komunikat o błędzie i kontynuować pracę.

stop = False
while(stop == False):
    x = input("Podaj liczbe (lub wpisz stop, żeby zakonczyc): ")

    if x == "stop":
        stop = True
        continue

    elif x.isdigit():
        x = int(x)
        print(pow(x, 3))

    else:
        print("Niepoprawna liczba całkowita")
