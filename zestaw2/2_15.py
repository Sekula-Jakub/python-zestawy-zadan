# Na liście L znajdują się liczby całkowite dodatnie.
# Stworzyć string będący ciągiem cyfr kolejnych liczb z listy L.

def stworz_string(l):
    result = ""
    for item in l:
        result += str(item)

    print(result)
    return result

L1 = [1, 2, 3, 4, 5, 6]
L2 = [9, 8, 1, 5, 8, 2]

assert stworz_string(L1) == "123456"
assert stworz_string(L2) == "981582"