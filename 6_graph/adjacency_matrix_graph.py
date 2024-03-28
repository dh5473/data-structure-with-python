class UndirectedGraph:
    def __init__(self, size):
        self.matrix = [[0] * size for _ in range(size)]
        self.size = size

    def __str__(self):
        elements = []
        for v1 in range(self.size):
            tmp = []
            for v2 in range(self.size):
                if self.matrix[v1][v2]:
                    tmp.append(v2)
            elements.append(tmp)
        return str(elements)

    def add_edge(self, v1, v2, w=1):
        if v1 >= self.size or v2 >= self.size:
            raise IndexError("matrix index out of range")
        
        if v1 == v2:
            raise ValueError(f"same vertex {v1} and {v2}")

        self.matrix[v1][v2] = w
        self.matrix[v2][v1] = w

    def remove_edge(self, v1, v2):
        if v1 >= self.size or v2 >= self.size:
            raise IndexError("matrix index out of range")
        
        if v1 == v2:
            raise ValueError(f"same vertex {v1} and {v2}")
        
        if not self.matrix[v1][v2] or not self.matrix[v2][v1]:
            raise ValueError(f"no edge between {v1} and {v2}")

        self.matrix[v1][v2] = 0
        self.matrix[v2][v1] = 0


class DirectedGraph:
    def __init__(self, size):
        self.matrix = [[0] * size for _ in range(size)]
        self.size = size

    def __str__(self):
        elements = []
        for v1 in range(self.size):
            tmp = []
            for v2 in range(self.size):
                if self.matrix[v1][v2]:
                    tmp.append(v2)
            elements.append(tmp)
        return str(elements)

    def add_edge(self, v1, v2, w=1):
        if v1 >= self.size or v2 >= self.size:
            raise IndexError("matrix index out of range")
        
        if v1 == v2:
            raise ValueError(f"same vertex {v1} and {v2}")

        self.matrix[v1][v2] = w

    def remove_edge(self, v1, v2):
        if v1 >= self.size or v2 >= self.size:
            raise IndexError("matrix index out of range")
        
        if v1 == v2:
            raise ValueError(f"same vertex {v1} and {v2}")
        
        if not self.matrix[v1][v2]:
            raise ValueError(f"no edge {v1} to {v2}")

        self.matrix[v1][v2] = 0