def fnumber(input_int):
    if input_int == 0:
        return 0
    elif input_int == 1:
        return 1
    else:
        return (fnumber(input_int - 1) + fnumber(input_int - 2))

print(fnumber(6))

def fibo4(n,l):
    if n == 0:
        return l[-2]
    if n == 1:
        return l[-1]
    else:
        l.append(l[-2]+l[-1])
        return fibo4(n-1,l)


print(fibo4(4,[0,1]))


def F(n, l = None):
    if l == None:
        l = [3,5,8]
    else:
        if n == 1:
            return l[0]
        elif n == 2:
            return l[1]
        elif n == 3:
            return l[2]
        else:
            return F(n - 1, l)

print(F(2))

def fibo1(n):
    l = [0,1]
    if n >= 2:
        for i in range (2,n):
            f = l[-2]+ l[-1]
            l.append(f)
    return l

print(fibo1(6))

def fib2(n):
    if n <= 1:
        return n
    else:
        num1 = 0
        num2 = 1
        for i in range(2,n + 1):
            num2 = num2 + num1
            num1 = num2 - num1

    return num2

print(fib2(3))