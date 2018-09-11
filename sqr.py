# def sqroot(integer,low,high,eps):
#     middle = (low + high)/2
#     if middle * middle > integer:
#         sqroot(integer,low,middle,eps)
#     if middle * middle < integer:
#         sqroot(integer,middle,high,eps)
#     else:
#         return middle
#


def sri(n,eps = 0.001):
    low = 0
    high = n
    mid = (low + high) / 2
    while (mid * mid - n).__abs__() > eps:
        if mid * mid > n:
            high = mid
        else:
            low = mid
        mid = (low + high) / 2
    return mid

print(sri(9))

def srr(n,eps,low = 0, high = 100):
    mid = (low + high)/ 2
    if (mid * mid -n).__abs__() < eps:
        return mid
    else:
        if mid * mid > n:
            high = mid
            return srr(n, eps, low, high)
        else:
            return srr(n,eps,mid,high)

print(srr(10,0.001,0,10))
