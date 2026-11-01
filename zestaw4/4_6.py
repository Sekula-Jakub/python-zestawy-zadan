# Napisać funkcję sum_seq(sequence) obliczającą sumę liczb zawartych w sekwencji, która może zawierać zagnieżdżone
# podsekwencje. Wskazówka: rozważyć wersję rekurencyjną, a sprawdzanie, czy element jest sekwencją, wykonać przez
# isinstance(item, (list, tuple)).

def sum_seq(sequence):
    total = 0
    for i in sequence:
        if isinstance(i, (list, tuple)):
            total += sum_seq(i)
        else:
            total += i
    return total

def test_sum_seq():
    print("test_sum_seq: ")
    sequence1 = [1, (2, 3), [4, (5, 6)], 7]
    sequence2 = [1, [2, [3, [4]]]]
    assert sum_seq([1, 2, 3, 4]) == 10
    assert sum_seq(sequence1) == 28
    assert sum_seq(sequence2) == 10
    print("Ok")

test_sum_seq()