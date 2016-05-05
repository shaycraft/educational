import random


def calc_p2(num):
    remainder = -1
    r = 0
    d = num
    while remainder != 1:
        quotient, remainder = divmod(d, 2)
        if remainder != 1:
            r += 1
            d = quotient
    assert(2**r * d == num)
    return {'r': int(r), 'd': int(d)}


def modular_pow(base, exponent, modulus):
    if modulus == 1:
        return 0
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent >>= 1
        base = (base * base) % modulus
    return result


# n is number to test for primality, k is accuracy
def miller_rabin(n, k):
    assert n >= 2
    if n == 2:
        return "Definitely prime"
    elif n % 2 == 0:
        return "Definitely composite"

    vals = calc_p2(n - 1)
    r = vals['r']
    d = vals['d']
    for i in range(0, k):
        a = random.randrange(2, n-1)
        x = modular_pow(a, d, n)
        if x != 1 and x != n - 1:
            stop = False
            for j in range(0, r - 1):
                x = modular_pow(x, 2, n)
                if x == 1:
                    return "x == 1 Composite"
                if x == n - 1:
                    stop = True
                    break
            if not stop:
                return "stop Composite"
    return "probably prime"

while True:
    in_str = input('N = ')
    print miller_rabin(long(in_str), 60)
