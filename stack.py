class Stack:
    def __init__(self):
        self.item = []

    def pop(self):
        return self.item.pop()

    def peek(self):
        return self.item[len(self.item) - 1]

    def push(self, item):
        self.item.append(item)

    def is_empty(self):
        return self.item == []

    def size(self):
        return len(self.item)

tryList = []
print(tryList.__eq__([]))

tryStack = Stack()
print(tryStack.is_empty())
tryStack.push(4)
tryStack.push('dog')
print(tryStack.peek())
tryStack.push(True)
print(tryStack.size())
print(tryStack.is_empty())
tryStack.push(8.4)
print(tryStack.pop())
print(tryStack.pop())
print(tryStack.size())
print(tryStack.pop())
print(tryStack.__eq__([4]))