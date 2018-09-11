def RecurMult(num_x,num_y):
    if num_x == 0 or num_y == 0:
        return 0
    elif num_x.__abs__() == 1:
        return num_y
    elif num_x > 0 and num_y > 0:
        return num_y + RecurMult(num_x -1, num_y)
    elif num_x < 0 and num_y < 0:
        return RecurMult(num_x.__abs__(),num_y.__abs__())
    else:
        return - RecurMult(num_x.__abs__(),num_y.__abs__())


def task1(a,b):
    if b == 0:
        return 0
    else:
        if b > 0:
            return a + task1(a, b - 1)
        else:
            return - task1(a, -b)