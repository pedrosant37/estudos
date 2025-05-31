class Stack:
    #Inicializa a Pilha
    def __init__(self):
        self.array = []

    #Mostra o último elemento da pilha
    def peek(self):
        if len(self.array) == 0:
            return None
        else:
            return self.array[-1]

    #Coloca um elemento na pilha
    def push(self, value):
        self.array.append(value)

    #Remove o último elemento da pilha
    def pop(self):
        if len(self.array) == 0:
            return None
        else:
            self.array.pop()
