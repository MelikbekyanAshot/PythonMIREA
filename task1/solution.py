from math import sqrt, cos, log


def f11(x, y, z):
    return 88*(z**5/77 - x**2 + 2)**7 + log(x) + z**4 - 43*z**8 - 40 + z**3 + sqrt((y**4 - log(x))/(cos(y) + 30*z**2))

def f12(x):
    if x < 72:
        return x**5 - 86*x - 94
    elif 72 <= x < 118:
        return 93*(x**4 - x**3 + 88)**8 - x
    else:
        return 87*(x**2 + 35*x**8)**8 + 74*x**7

def f13(n, m):
    a = 0
    for i in range (1, n+1):
        for j in range(1, m+1):
            a += (j - 62*i**5)

    b = 0
    for i in range (1, n+1):
        for j in range(1, m+1):
            b += (62*i**3 + j**2)

    return a - b

def f14(n):
    if n == 0:
        return 5
    else:
        return 1/78 * f14(n-1) + 1/93 * f14(n-1)**2 -78