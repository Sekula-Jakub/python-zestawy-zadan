import math

# założeniem jest, że w każdym ułamku minus powinien być przy liczniku oraz ułamek powinien być maksymalnie skrócony
def minimize_fraction(frac):
    if frac[1] < 0:
        frac[0] *= -1
        frac[1] *= -1

    gcd = math.gcd(frac[0], frac[1])
    frac[0] //= gcd
    frac[1] //= gcd

def lcm(a, b):
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // math.gcd(a, b)

def common_denominator(frac1, frac2):
    minimize_fraction(frac1)
    minimize_fraction(frac2)

    least_common_multiple = lcm(frac1[1], frac2[1])

    frac1[0] *= least_common_multiple // frac1[1]
    frac2[0] *= least_common_multiple // frac2[1]

    frac1[1] = least_common_multiple
    frac2[1] = least_common_multiple

def add_frac(frac1, frac2):
    common_denominator(frac1, frac2)
    answer = [frac1[0] + frac2[0], frac1[1]]
    minimize_fraction(answer)
    return answer

def sub_frac(frac1, frac2):
    common_denominator(frac1, frac2)
    answer = [frac1[0] - frac2[0], frac1[1]]
    minimize_fraction(answer)
    return answer

def mult_frac(frac1, frac2):
    answer = [frac1[0] * frac2[0], frac1[1] * frac2[1]]
    minimize_fraction(answer)
    return answer

def div_frac(frac1, frac2):

    if frac2[0] == 0:
        raise ZeroDivisionError

    temp = frac2[0]
    frac2[0] = frac2[1]
    frac2[1] = temp
    minimize_fraction(frac1)
    return mult_frac(frac1, frac2)

def is_positive(frac):
    minimize_fraction(frac)
    return frac[0] > 0

def is_zero(frac):
    minimize_fraction(frac)
    return frac[0] == 0 or frac[1] == 0

def cmp_frac(frac1, frac2):
    minimize_fraction(frac1)
    minimize_fraction(frac2)

    common_denominator(frac1, frac2)

    if frac1[0] < frac2[0]:
        return -1
    elif frac1[0] > frac2[0]:
        return 1
    else:
        return 0

def frac2float(frac):
    minimize_fraction(frac)
    return frac[0] / frac[1]