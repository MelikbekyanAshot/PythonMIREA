def f(n, m):
    a = 0
    for i in range (1, n+1):
        for j in range(1, m+1):
            a += (j - 62*i**5)

    b = 0
    for i in range (1, n+1):
        for j in range(1, m+1):
            b += (62*i**3 + j**2)

    return a - b


print('%.2e' % f(82, 31))
print('%.2e' % f(72, 25))