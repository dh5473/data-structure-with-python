class HashTable:
    def __init__(self, capacity=4, load_factor=0.66):
        if not capacity:
            raise ValueError("zero capacity is not accepted")

        self.capacity = capacity
        self.table = [None] * capacity
        self.load_factor = load_factor
        self.size = 0

    def __str__(self):
        elements = []
        for idx in range(self.capacity):
            elements.append((self.table[idx][0], self.table[idx][1]))
        
        return str(elements)

    def _hash(self, key):
        return hash(key) % self.capacity

    def insert(self, key, value):
        idx = self._hash(key)

        step = 1
        while self.table[idx] is not None:
            if self.table[idx][0] == key:
                self.table[idx][1] = value
                break
            idx = (idx + step ** 2) % self.capacity
            step += 1
        else:
            self.table[idx] = (key, value)

        self.size += 1

        if (self.size / self.capacity) > self.load_factor:
            self.rehash()

    def search(self, key):
        idx = self._hash(key)

        step = 1
        while self.table[idx] is not None:
            if self.table[idx][0] == key:
                return self.table[idx][1]
            idx = (idx + step ** 2) % self.capacity
            step += 1
        
        raise KeyError(key)

    def remove(self, key):
        idx = self._hash(key)

        step = 1
        while self.table[idx] is not None:
            if self.table[idx][0] == key:
                self.table[idx] = None
                self.size -= 1
                return
            idx = (idx + step ** 2) % self.capacity
            step += 1
        
        raise KeyError(key)

    def rehash(self):
        prev_table = self.table
        prev_capacity = self.capacity

        self.capacity *= 2
        self.table = [None] * self.capacity
        self.size = 0

        for idx in range(prev_capacity):
            self.insert(prev_table[idx][0], prev_table[idx][1])