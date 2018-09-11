class BinaryTree:
    def __init__(self, key):
        self.key = key
        self.leftChild = None
        self.rightChild = None

    def __str__(self):
        return str(self.key)

    def setLeftChild(self, tree):
        assert self.hasLeftChild() is False
        self.leftChild = tree

    def setRightChild(self, tree):
        assert self.hasRightChild() is False
        self.rightChild = tree

    def getLeftChild(self):
        assert self.hasLeftChild()
        return self.leftChild

    def getRightChild(self):
        assert self.hasRightChild()
        return self.rightChild

    def hasLeftChild(self):
        return True if self.leftChild is not None else False

    def hasRightChild(self):
        return True if self.rightChild is not None else False

    def preorderPrint(self):
        print(self.key)
        if self.leftChild is not None:
            self.leftChild.preorderPrint()
        if self.rightChild is not None:
            self.rightChild.preorderPrint()

    def postorderPrint(self):
        if self.leftChild is not None and self.rightChild is not None:
            self.getLeftChild().postorderPrint()
            self.getRightChild().postorderPrint()

        print(self.key)


    def inorderPrint(self):
        if self.leftChild is not None and self.rightChild is not None:
            self.getLeftChild().inorderPrint()
            print(self.key)
            self.getRightChild().inorderPrint()


def buildTree1():
    tree = BinaryTree(7)
    tree.setLeftChild(BinaryTree(8))
    tree.getLeftChild().setLeftChild(BinaryTree(12))
    tree.getLeftChild().getLeftChild().setLeftChild(BinaryTree(5))
    tree.getLeftChild().getLeftChild().setRightChild(BinaryTree(10))
    tree.getLeftChild().setRightChild(BinaryTree(9))
    #right of the tree
    tree.setRightChild(BinaryTree(7))
    tree.getRightChild().setLeftChild(BinaryTree(5))
    tree.getRightChild().setRightChild(BinaryTree(6))
    return tree


T1 = buildTree1()
T1.preorderPrint()
print()
T1.postorderPrint()
print()
T1.inorderPrint()