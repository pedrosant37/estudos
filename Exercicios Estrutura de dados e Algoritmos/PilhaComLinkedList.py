class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    #Inicializa a Pilha
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    #Mostra o último elemento da pilha
    def peek(self):
        if self.length == 0:
            return None
        else:
            return self.top

    #Coloca um elemento na pilha
    def push(self, value):
        node = Node(value)
        if self.length == 0:
            self.bottom = node
            self.top = node
        else:
            temp = self.top
            self.top = node
            self.top.next = temp
        self.length += 1

    #Retira o último elemento da pilha
    def pop(self):
        if self.length == 0:
            return None
        self.top = self.top.next
