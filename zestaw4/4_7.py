# Mamy daną sekwencję, w której niektóre z elementów mogą okazać się podsekwencjami, a takie zagnieżdżenia mogą się
# nakładać do nieograniczonej głębokości. Napisać funkcję flatten(sequence), która zwróci spłaszczoną listę wszystkich
# elementów sekwencji. Wskazówka: rozważyć wersję rekurencyjną, a sprawdzanie czy element jest sekwencją, wykonać przez
# isinstance(item, (list, tuple)).

# sequence = [1,(2,3),[],[4,(5,6,7)],8,[9]]
# print(flatten(sequence))   # [1,2,3,4,5,6,7,8,9]

def flatten(sequence):
    result = []
    for item in sequence:
        if isinstance(item, (list, tuple)):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

def test_flatten():
    print("test_flatten: ")
    sequence1 = [1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]
    sequence2 = [1, (2, [3, (4, 5), []]), 6, (7, 8), [[], 9]]
    assert flatten(sequence1) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert flatten(sequence2) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("ok")

test_flatten()
