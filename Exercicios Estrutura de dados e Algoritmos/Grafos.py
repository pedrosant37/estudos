class Graph:
    def __init__(self):
        self.numberOfNodes = 0
        self.adjacentList = {}

    def addVertex(self, node):
        if node in self.adjacentList:
            return None
        self.adjacentList[node] = []

    def addEdge(self, node1, node2):
        if node1 == node2:
            return None
        if node2 in self.adjacentList[node1]:
            return None
        else:
            self.adjacentList[node1].append(node2)
            self.adjacentList[node2].append(node1)

    def showConnections(self):
        for k in self.adjacentList:
            print()
            print(k, ' --> ', end='')
            for v in range(0, len(self.adjacentList[k])):
                print(self.adjacentList[k][v], end=' ')

