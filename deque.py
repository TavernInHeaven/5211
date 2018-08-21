class Deque:
    def __init__(self):
        self.item = []

    def size(self):
        return len(self.item)

    def is_empty(self):
        return self.item == []

    def add_front(self,item):
        self.item.insert(0,item)

    def add_rear(self,item):
        self.item.append(item)

    def remove_front(self):
        self.item.pop(0)

    def remove_rear(self):
        self.item.pop()

