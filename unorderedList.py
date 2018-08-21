from node import Node

class UnorderedList:
    def __init__(self):
        self.head = None

    def is_empyt(self):
        return self.head == None

    def add(self,item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()

        return count

    def search(self,item):
        current = self.head
        found = False
        while current is not None and found is False:
            if current.get_data() is item:
                found = True
            else:
                current = current.get_next()

        return found

mylist = UnorderedList()
mylist.add(1)
mylist.add(2)
mylist.add(3)
mylist.add(4)
print(mylist.search(5))

