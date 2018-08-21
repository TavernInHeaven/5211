def dp(n):
    l = [None] * (n + 1)
    l[0] = ""
    for i in range(1, n + 1):
        #l[i] = str(n + 1 - i) + "\n" + str(dp(n - 1)) + str(dp(n))
        l[i] = str(i) + "\n" + l[i - 1] + l[i // 2]
    print(l[n])

#l[i] = str(i) + "\n" + l[i - 1] + l[i // 2]

dp(5)


def ways(n, mem = None):
    #calls = 1
    if mem is None:
        mem = [None] * (n + 1)

    mem[n] = 1
    for i in range(1, n):
        if mem[i] is None:
            (w) = ways(i)
        else:
            w = mem[i]
            c = 0
        mem[n] += w
        #calls += c
    return (mem[n])#, calls)

print(ways(4))
print("-")


def count(n):
    cl = [None] * (n + 1)
    sum = 1
    for i in range(1, n + 1):
        cl[i] = ways(i)
    for i in range(1, n):
        sum += cl[i]
    return sum,cl


print(count(1))
print(count(2))
print(count(3))
print(count(4))
print(count(5))
print(count(6))