import math
import random


def calc_p2(num):
    if num % 2 == 1:
        raise "ERROR:  num must be even"
    for d in range(1, num + 1, 2):
        print d
        r = math.log(float(num)/float(d)) / math.log(2)
        print r
        if r.is_integer():
            return {'r': int(r), 'd': int(d)}


# n is number to test for primality, k is accuracy
def miller_rabin(n, k):
    vals = calc_p2(n - 1)
    r = vals['r']
    d = vals['d']
    for i in range(0, k):
        print "DEBUG:  beginning of i while loop"
        a = random.choice([x for x in range(2, n - 1)])
        # the following should be improved with repeated squaring-modular exponentiation for real-world usage
        x = pow(a, d) % n
        if x != 1 and x != n - 1:
            stop = False
            for j in range(0, r - 1):
                print "DEBUG:  beginning of j while loop"
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


miller_rabin(223, 60)
