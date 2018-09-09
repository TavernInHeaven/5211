def fib2(n, l = None):
    if l == None:
        l = [3, 5, 8]
    if n < len(l):
        return l[n]
    else:
        f = fib2(n - 3, l) + 2 * fib2(n - 2, l)
        if n < len(l):
            l.append(fib2(len(l)))
            print(l)
        return f

print(fib2(10))

def fib3(n,l = None):
    if l == None:
        l = [3, 5, 8]
    if n > len(l):
        l[len(l)] = fib3(len(l))

    f = 2 * fib3(n - 2) + fib3(n - 3)
    return f

print(fib3(3))

def fib(n, l = None):
    if l is None:
        l = [None] * max(3, n + 1)
        l[0] = 3
        l[1] = 5
        l[2] = 8

    if l[n] is None:
        l[n] = 2 * l[n - 2] + l[n - 3]
    return l[n]



print(fib(4))