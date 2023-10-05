def rev(n, a):
    if n == 0:
        return a

    a = 10 * a + n % 10

    return rev(n // 10, a)


print(rev(653, 0))
