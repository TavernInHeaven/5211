def mul(x,y):
    if x == 0 or y == 0:
        return 0
    else:
        if x > 0:
            return y + mul(x - 1, y)
        else:
            return - y + mul(-x - 1, -y)


print(mul(-3,-4))
for x in range(-100,100):
    for y in range(-100,100):
        assert (mul(x,y) == x*y)


#deque

class Deque():
    def __init__(self):
        self.deque = []

    def is_empty(self):
        return self.deque == []

    def length(self):
        return len(self.deque)

    def addFront(self,ch):
        self.deque.insert(0, ch)

    def addRear(self,ch):
        self.deque.append(ch)

    def removeFront(self):
        self.deque.pop(0)

    def removeRear(self):
        self.deque.pop()


def palChecker(astring):
    deque = Deque

    for ch in astring:
        deque.addRear(ch)

    return dequePalCheck(deque)


def dequePalCheck(deque):
    if deque.length() <= 1:
        return True
    elif deque.removeFront() == deque.removeRear():
        return palChecker(deque)
    else:
        return False

print(palChecker("TimiT"))