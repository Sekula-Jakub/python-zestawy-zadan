# Napisać iteracyjną wersję funkcji factorial(n) obliczającej silnię.

def factorial(n):
    if n == 0:
        return 1

    answer = 1
    for i in range(1, n+1):
        answer *= i

    return answer

def test_factorial():
    print("testy dla factorial:")
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(3) == 6
    assert factorial(5) == 120
    assert factorial(6) == 720
    print("ok")

test_factorial()
