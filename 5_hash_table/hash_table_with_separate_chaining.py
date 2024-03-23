class Node:
    def __init__(self, key, value, next=None):
        self.key = key
        self.value = value
        self.next = next


class HashTable:
    def __init__(self, capacity=4, load_factor=0.75):
        if not capacity:
            raise ValueError("zero capacity is not accepted")

        self.capacity = capacity
        self.table = [None] * capacity
        self.load_factor = load_factor
        self.size = 0

    def __str__(self):
        elements = []
        for idx in range(self.capacity):
            curr_node: Node = self.table[idx]
            while curr_node:
                elements.append((curr_node.key, curr_node.value))
                curr_node = curr_node.next

        return str(elements)

    def _hash(self, key):
        return hash(key) % self.capacity

    def insert(self, key, value):
        idx = self._hash(key)

        if self.table[idx] is None:
            self.table[idx] = Node(key, value)
        else:
            curr_node: Node = self.table[idx]
            while curr_node:
                if curr_node.key == key:
                    curr_node.value = value
                    return
                curr_node = curr_node.next
            curr_node = Node(key, value)
        
        self.size += 1

        if (self.size / self.capacity) > self.load_factor:
            self.rehash()

    def search(self, key):
        idx = self._hash(key)

        curr_node: Node = self.table[idx]
        while curr_node:
            if curr_node.key == key:
                return curr_node.value
            curr_node = curr_node.next
        
        raise KeyError(key)

    def remove(self, key):
        idx = self._hash(key)

        prev_node: Node = None
        curr_node: Node = self.table[idx]
        while curr_node:
            if curr_node.key == key:
                if prev_node:
                    prev_node.next = curr_node.next
                else:
                    self.table[idx] = curr_node.next
                self.size -= 1
                return
            prev_node = curr_node
            curr_node = curr_node.next
        
        raise KeyError(key)

    def rehash(self):
        prev_table = self.table
        prev_capacity = self.capacity

        self.capacity *= 2
        self.table = [None] * self.capacity
        self.size = 0

        for idx in range(prev_capacity):
            curr_node: Node = prev_table[idx]
            while curr_node:
                self.table.insert(curr_node.key, curr_node.value)
                curr_node = curr_node.next