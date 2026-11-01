# Napisać funkcję odwracanie(L, left, right) odwracającą kolejność elementów na liście od numeru left do right
# włącznie. Lista jest modyfikowana w miejscu (in place). Rozważyć wersję iteracyjną i rekurencyjną.

def odwracanie(L, left, right):
    while left <= right:
        temp = L[left]
        L[left] = L[right]
        L[right] = temp

        left += 1
        right -= 1
    return L

def odwracanie_rekurencyjne(L, left, right):
    if left >= right:
        return
    temp = L[left]
    L[left] = L[right]
    L[right] = temp

    odwracanie_rekurencyjne(L, left + 1, right - 1)


def test_odwracanie():
    print("Test odwracanie iteracyjne: ")
    list1 = [6, 7, 2, 1, 3, 7, 8, 4]
    list2 = [9, 0, 1, 2, 6, 9, 2]
    assert odwracanie(list1, 2, 6) == [6, 7, 8, 7, 3, 1, 2, 4]
    assert odwracanie(list2, 0, 2) == [1, 0, 9, 2, 6, 9, 2]
    print("Ok")

    list1 = [6, 7, 2, 1, 3, 7, 8, 4]
    list2 = [9, 0, 1, 2, 6, 9, 2]
    print("Test odwracanie rekurencyjne: ")
    odwracanie_rekurencyjne(list1, 2, 6)
    odwracanie_rekurencyjne(list2, 0, 2)
    assert list1 == [6, 7, 8, 7, 3, 1, 2, 4]
    assert list2 == [1, 0, 9, 2, 6, 9, 2]
    print("Ok")

test_odwracanie()