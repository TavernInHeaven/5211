def fib(n, l=None):
    if l is None:
        l = [None] * max(3, n + 1)
        l[0] = 3
        l[1] = 5
        l[2] = 8

    if l[n] is None:
        l[n] = 2 * fib(n - 2, l) + fib(n - 3, l)

    return l[n]


print(fib(7))