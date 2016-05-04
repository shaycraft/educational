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
        a = random.choice([x for x in range(2, n - 1)])
        # the following should be improved with repeated squaring-modular exponentiation for real-world usage
        x = pow(a, d) % n
        if x != 1 and x != n - 1:
            stop = False
            for j in range(0, r - 1):
                x = pow(x, 2) % n
                if x == 1:
                    print "Composite"
                    return
                if x == n - 1:
                    stop = True
            if not stop:
                print "Composite"
                return
    print "probably prime"
    return


miller_rabin(7881, 60)
