def fib(n):
    memo = [1, 1]
    if n < len(memo):
        return memo[n]

    if n < 2:
        return 1
    else:
        f = fib(n - 1) + fib(n - 2)
        memo.append(f)
        return f

#print(fib(6))


