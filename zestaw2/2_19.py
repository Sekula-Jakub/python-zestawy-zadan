# Na liście L mamy liczby jedno-, dwu- i trzycyfrowe dodatnie. Chcemy zbudować string z trzycyfrowych bloków,
# gdzie liczby jedno- i dwucyfrowe będą miały blok dopełniony zerami, np. 007, 024. Wskazówka: str.zfill().

def dopelnij_do_trzech(lista):
    print(lista)
    answer = ""
    for l in lista:
        answer += str(l).zfill(3)
    print(answer)
    return answer

L1 = [123, 78, 67, 4, 12, 901]
L2 = [120, 940, 12, 9, 1, 7, 18]\

assert dopelnij_do_trzech(L1) == "123078067004012901"
assert dopelnij_do_trzech(L2) == "120940012009001007018"

