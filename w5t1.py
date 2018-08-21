def dp(n):
    l = [None] * (n + 1)
    for i in range(1, n + 1):
        l[i] = str(i + 1) + "\n" + str(i)  + str(i - 1)
    print(l[n])



dp(5)


