# Napisać iteracyjną wersję funkcji fibonacci(n) obliczającej n-ty wyraz ciągu Fibonacciego.

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    a = 0
    b = 1
    for i in range(2, n+1):
        c = a + b
        a = b
        b = c

    return c

def test_fibbonacci():
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(12) == 144
    assert fibonacci(16) == 987

test_fibbonacci()