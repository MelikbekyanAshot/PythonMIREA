from math import sqrt, cos, log


def f(x, y, z):
    return 88*(z**5/77 - x**2 + 2)**7 + log(x) + z**4 - 43*z**8 - 40 + z**3 + sqrt((y**4 - log(x))/(cos(y) + 30*z**2))

print('%.2e' % f(55, -25, -12))
print('%.2e' % f(51, -30, -87))