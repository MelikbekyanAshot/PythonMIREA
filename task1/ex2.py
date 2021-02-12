def f(x):
    if x < 72:
        return x**5 - 86*x - 94
    elif 72 <= x < 118:
        return 93*(x**4 - x**3 + 88)**8 - x
    else:
        return 87*(x**2 + 35*x**8)**8 + 74*x**7

print('%.2e' % f(190))
print('%.2e' % f(75))