class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def enqueue(self, value):
        node = Node(value)
        if self.length == 0:
            self.last = node
            self.first = node
        else:
            self.last.next = node
            self.last = self.last.next
        self.length += 1

    def dequeue(self):
        if self.length == 0:
            return None
        self.first = self.first.next
        self.length -= 1

    def peek(self):
        if self.length == 0:
            return None
        return self.first.value

