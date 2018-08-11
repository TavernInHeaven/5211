def recursion(number):
    print(number)
    if number > 1:
        recursion(number - 1)
        recursion(number // 2)

print(recursion(5))