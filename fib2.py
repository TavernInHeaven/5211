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


def recursivelog(n, x, b, l = None, u = None):
    assert( n >= 0)
    assert( x >= 1)
    assert( isinstance(b, int) )
    assert( b >= 2 )
    if l is None:
        l = 0
    if u is None:
        u = 10

    #guess = round((u + l) / 2.0, 8)
    guess = (u + l) / 2.0

    if n == 0:
        return guess

    if b ** guess > x:
        return recursivelog(n - 1, x, b, l, guess)
    elif b ** guess < x:
        if b ** u < x:
            return recursivelog(n - 1, x, b, l + 10, u + 10)
        else:
            return recursivelog(n - 1, x, b, guess, u)
    else:
        return guess


print(recursivelog(100, 4194305, 2))