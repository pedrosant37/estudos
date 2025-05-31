class Node:
    def __init__(self, value):
        self.right = None
        self.left = None
        self.value = value

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            node = Node(value)
            currentNode = self.root
            while True:
                if node.value > currentNode.value:
                    if currentNode.right is None:
                        currentNode.right = node
                        break
                    else:
                        currentNode = currentNode.right
                elif node.value < currentNode.value:
                    if currentNode.left is None:
                        currentNode.left = node
                        break
                    else:
                        currentNode = currentNode.left
                else:
                    return None
    def lookup(self, value):
        if self.root is None:
            return False
        currentNode = self.root
        while currentNode.value != value:
            if value < currentNode.value and currentNode.left is not None:
                currentNode = currentNode.left
            elif value > currentNode.value and currentNode.right is not None:
                currentNode = currentNode.right
            else:
                return False
        return currentNode
    def traverseInOrder(self, root):
        if root.left is not None:
            self.traverseInOrder(root.left)
        print(root.value)
        if root.right is not None:
            self.traverseInOrder(root.right)

    def traversePreOrder(self, root):
        print(root.value)
        if root.left is not None:
            self.traversePreOrder(root.left)
        if root.right is not None:
            self.traversePreOrder(root.right)

    def traversePostOrder(self, root):
        if root.left is not None:
            self.traversePostOrder(root.left)
        if root.right is not None:
            self.traversePostOrder(root.right)
