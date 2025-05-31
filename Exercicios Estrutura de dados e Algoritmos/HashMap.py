from LinkedListSimples import LinkedList

class HashMap:
    def __init__(self, size=100):
        self.size = size
        self.array = [LinkedList() for _ in range(size)]

    # Hasheia uma key e retorna ela dividida pelo resto do tamanho da lista
    def _hash(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        index = self._hash(key)
        linkedlist = self.array[index]
        currentKey = linkedlist.searchKey(key)
        if currentKey:
            currentKey['value'] = value
        else:
            linkedlist.prepend([key, value])
