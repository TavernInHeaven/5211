class Node:
    def __init__(self, init_data=None):
        self.data = init_data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, data):
        self.data = data

    def set_next(self, next):
        self.next = next

node_1 = Node(3)
node_2 = Node(4)

node_1.set_next(node_2)
print(node_1.get_data(), node_1.get_next().get_data())

