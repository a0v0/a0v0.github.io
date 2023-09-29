def f(*args):
    s = 1
    for i in args:
        s *= i
    print(s)


f(1, 2, 3)
f(1, 3, 3)
