class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 1

    # Percorre na lista até um dado índice
    def traverseToIndex(self, index):
        counter = 0
        currentNode = self.head
        while index != counter:
            currentNode = currentNode.next
            counter += 1
        return currentNode

    # Adiciona um elemento no final da lista
    def append(self, value):
        if self.head is None:
            node = Node(value)
            self.head = node
            self.tail = node
            self.length += 1
            return

        tempNode = Node(value)
        self.tail.next = tempNode
        tempNode.previous = self.tail
        self.tail = tempNode
        self.length += 1

    # Adiciona um elemento no começo da lista
    def prepend(self, value):
        if self.head is None:
            node = Node(value)
            self.head = node
            self.tail = node
            self.length += 1
            return

        tempNode = Node(value)
        tempNode.next = self.head
        self.head = tempNode
        self.length += 1

    # Adiciona um elemento na lista em um dado índice
    def insert(self, index, value):
        if index >= self.length:
            return self.append(value)
        elif index <= 0:
            return self.prepend(value)
        tempNode = Node(value)
        currentNode = self.traverseToIndex(index-1)
        nextNode = currentNode.next
        currentNode.next = tempNode
        tempNode.next = nextNode
        tempNode.previous = currentNode

        self.length += 1

    # Remove um elemento de um dado índice da lista
    def remove(self, index):
        if index >= self.length or index <= 0:
            raise IndexError
        leader = self.traverseToIndex(index-1)
        unwantedNode = leader.next
        afterNode = unwantedNode.next
        leader.next = afterNode
        afterNode.previous = leader
        self.length -= 1
