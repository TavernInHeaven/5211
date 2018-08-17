def F(n, l = None):
    if l == None:
        l = [3,5,8]

    if n < 4:
        return l[n - 1]
    else:
        if n > len(l) + 1:
            next_item = 2 * F(len(l) - 1, l) + F(len(l) - 2, l)
            l.append(next_item)

    return 2 * l[-2] + l[-3]


print(F(6))