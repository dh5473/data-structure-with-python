class Node:
    def __init__(self, idx, val=None, next=None):
        self.idx = idx
        self.val = val
        self.next = next


class UndirectedGraph:
    def __init__(self, size):
        self.array = [None] * size
        self.size = size
    
    def __str__(self):
        elements = dict()
        for idx in range(self.size):
            elements[idx] = []
            curr_node: Node = self.array[idx]
            if curr_node:
                curr_node = curr_node.next
            while curr_node:
                elements[idx].append(curr_node.idx)
                curr_node = curr_node.next
            elements[idx].sort()
        return str(elements)

    def add_edge(self, v1, v2, w=1):
        if v1 >= self.size or v2 >= self.size:
            raise IndexError("array index out of range")

        if v1 == v2:
            raise ValueError(f"same vertex {v1} and {v2}")

        if self.array[v1] is None:
            node = Node(v1)
            self.array[v1] = node
        
        curr_node: Node = self.array[v1]
        while curr_node:
            if curr_node.next is None:
                if curr_node.idx == v2:
                    break
                new_node = Node(v2, w)
                curr_node.next = new_node
                break
            curr_node = curr_node.next

        if self.array[v2] is None:
            node = Node(v2)
            self.array[v2] = node
        
        curr_node: Node = self.array[v2]
        while curr_node:
            if curr_node.next is None:
                if curr_node.idx == v1:
                    break
                new_node = Node(v1, w)
                curr_node.next = new_node
                break
            curr_node = curr_node.next

    def remove_edge(self, v1, v2):
        if v1 >= self.size or v2 >= self.size:
            raise IndexError("array index out of range")
        
        if v1 == v2:
            raise ValueError(f"same vertex {v1} and {v2}")

        prev_node: Node = None
        curr_node: Node = self.array[v1]
        while curr_node:
            if curr_node.idx == v2:
                prev_node.next = curr_node.next
                break
            curr_node = curr_node.next
            prev_node = curr_node
        else:
            raise ValueError(f"no edge between {v1} and {v2}")
        
        prev_node: Node = None
        curr_node: Node = self.array[v2]
        while curr_node:
            if curr_node.idx == v1:
                prev_node.next = curr_node.next
                break
            curr_node = curr_node.next
            prev_node = curr_node
        else:
            raise ValueError(f"no edge between {v2} and {v1}")


class DirectedGraph:
    def __init__(self, size):
        self.array = [None] * size
        self.size = size
    
    def __str__(self):
        elements = dict()
        for idx in range(self.size):
            elements[idx] = []
            curr_node: Node = self.array[idx]
            if curr_node:
                curr_node = curr_node.next
            while curr_node:
                elements[idx].append(curr_node.idx)
                curr_node = curr_node.next
            elements[idx].sort()
        return str(elements)

    def add_edge(self, v1, v2, w=1):
        if v1 >= self.size or v2 >= self.size:
            raise IndexError("array index out of range")

        if v1 == v2:
            raise ValueError(f"same vertex {v1} and {v2}")

        if self.array[v1] is None:
            node = Node(v1)
            self.array[v1] = node
        
        curr_node: Node = self.array[v1]
        while curr_node:
            if curr_node.next is None:
                if curr_node.idx == v2:
                    break
                new_node = Node(v2, w)
                curr_node.next = new_node
                break
            curr_node = curr_node.next

    def remove_edge(self, v1, v2):
        if v1 >= self.size or v2 >= self.size:
            raise IndexError("array index out of range")
        
        if v1 == v2:
            raise ValueError(f"same vertex {v1} and {v2}")

        prev_node: Node = None
        curr_node: Node = self.array[v1]
        while curr_node:
            if curr_node.idx == v2:
                prev_node.next = curr_node.next
                break
            curr_node = curr_node.next
            prev_node = curr_node
        else:
            raise ValueError(f"no edge {v1} to {v2}")