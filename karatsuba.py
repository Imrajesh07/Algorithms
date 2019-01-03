import math
import time

def karatsuba_mult(x, y):
    """
    Karatsuba multiplication Algorithm implementation.

    """

    p = str(x)
    q = str(y)

    n1 = len(p)
    n2 = len(q)

    if n1 != n2:

        if n1 < n2:
            p = "0" * (n2 - n1) + p
            n = n2

        else:
            q = "0" * (n1 - n2) + q
            n = n1
    
    else:
        n = n1

    if n == 1:
        return x * y

    else:
        a = int(p[:math.ceil(n/2)])
        b = int(p[math.ceil(n/2):])
        c = int(q[:math.ceil(n/2)])
        d = int(q[math.ceil(n/2):])

        ac = karatsuba_mult(a, c)
        bd = karatsuba_mult(b, d) 
        ad_plus_bc = karatsuba_mult((a + b), (c + d)) - ac - bd
        result = int(str(ac) + "0" * (n // 2) * 2) + int(str(ad_plus_bc) + "0" * (n // 2)) + bd

        return result

t1 = time.time()
print(karatsuba_mult(3141592653589793238462643383279502884197169399375105820974944592, 2718281828459045235360287471352662497757247093699959574966967627))
t2 = time.time()

t3 = time.time()
print(3141592653589793238462643383279502884197169399375105820974944592 * 2718281828459045235360287471352662497757247093699959574966967627)
t4 = time.time()

print((t2 - t1) - (t4 - t3))
