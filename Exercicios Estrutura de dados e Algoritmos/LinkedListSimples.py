class LinkedList:
    def __init__(self, value=None):
        # Primeiro elemento da lista
        self.head = {
            'value':value,
            'next': None
        }
        # Cauda da lista
        self.tail = self.head
        self.length = 1

    # Adiciona um elemento no final da lista
    def append(self, value):
        newNode = {
            'value':value,
            'next':None
        }
        self.tail['next'] = newNode
        self.tail = newNode
        self.length += 1

    # Adiciona um elemento no começo da lista
    def prepend(self, value):
        newNode = {
            'value':value,
            'next': self.head
        }
        self.head = newNode
        self.length += 1

    # Insere um elemento em um dado lugar da lista
    def insert(self,index, value):
        if index <= 0:
            return self.prepend(value)
        if index >= self.length:
            return self.append(value)

        newNode = {
            'value':value,
            'next': None
        }
        cont = 0
        start = self.head
        while cont != index-1:
            start = start['next']
            cont += 1
        posNode = start['next']
        start['next'] = newNode
        newNode['next'] = posNode

    # Reverte a Lista
    def reverse(self):
        if self.length == 1:
            return self.head

        firstNode = self.head
        nextNode = self.head['next']
        self.tail = firstNode
        while nextNode['next'] is not None:
            temp = nextNode['next']
            nextNode['next'] = firstNode
            firstNode = nextNode
            nextNode = temp
        nextNode['next'] = firstNode
        self.head = nextNode
        self.tail['next'] = None
