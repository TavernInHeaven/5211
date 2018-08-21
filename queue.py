class Queue:
    def __init__(self):
        self.item = []

    def is_empty(self):
        return self.item == []

    def size(self):
        return len(self.item)

    def enque(self,item):
        self.item.append(item)

    def deque(self):
        self.item.pop(0)