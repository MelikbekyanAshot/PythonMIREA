def f(n):
    if n == 0:
        return 5
    else:
        return 1/78 * f(n-1) + 1/93 * f(n-1)**2 - 78

print('%.2e' % f(9))
print('%.2e' % f(5))
print(f(0))