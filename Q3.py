def pair_search(l, p):
    found = False
    calls = 1
    #............
    lenthl = len(l)
    if l[0] == p:
        found = True
    elif lenthl > 1 and l[lenthl // 2] > p:
        pair_search(l[:lenthl // 2], p)
    elif lenthl > 1 and l[lenthl // 2] < p:
        pair_search(l[lenthl // 2:], p)
    else:
        found = False
    return found, calls


l = [1,2,3,4,5,6,7,8,9,10]
p = 7
print(pair_search(l,p))