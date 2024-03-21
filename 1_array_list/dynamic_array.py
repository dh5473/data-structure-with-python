class ArrayList:
    def __init__(self):
        self.array = [None]
        self.capacity = 1
        self.size = 0

    def __len__(self):
        return self.size
    
    def __str__(self):
        return str(self.array[:self.size])
    
    def __getitem__(self, idx):
        self._validate_index(idx)
        return self.array[idx]
    
    def to_list(self):
        return self.array[:self.size]

    def append(self, item):
        if self.size == self.capacity:
            self.resize_list()
        
        self.array[self.size] = item
        self.size += 1

    def extend(self, iterable):
        for item in iterable:
            self.append(item)

    def insert(self, idx, item):
        if idx == self.size:
            self.append(item)
            return
        self._validate_index(idx)
        
        if self.size == self.capacity:
            self.resize_list()
        
        for i in range(self.size, idx, -1):
            self.array[i] = self.array[i-1]
        
        self.array[idx] = item
        self.size += 1

    def remove(self, item):
        for i in range(self.size):
            if self.array[i] == item:
                idx = i
                break
        else:
            raise ValueError("array.remove(x): x not in array")
        
        for i in range(idx, self.size-1):
            self.array[i] = self.array[i+1]
        self.array[self.size] = None
        self.size -= 1

    def pop(self, idx=None):
        if idx is None:
            idx = self.size - 1

        if self.size == 0:
            raise IndexError("pop from empty array")
        self._validate_index(idx)

        item = self.array[idx]
        for i in range(idx, self.size-1):
            self.array[i] = self.array[i+1]
        self.array[self.size] = None
        self.size -= 1

        return item

    def clear(self):
        self.array = [None]
        self.capacity = 1
        self.size = 0

    def index(self, item):
        for idx in range(self.size):
            if self.array[idx] == item:
                return idx
        raise ValueError(f"{item} is not in array")

    def count(self, item):
        cnt = 0
        for i in range(self.size):
            if self.array[i] == item:
                cnt += 1
        return cnt
    
    def sort(self):
        self.array = sorted(self.array[:self.size])
    
    def reverse(self):
        self.array = self.array[:self.size][::-1]
    
    def copy(self):
        return self.array[:self.size]

    def resize_list(self):
        new_array = [None] * (self.size * 2)
        self.capacity = self.size * 2
        for idx in range(self.size):
            new_array[idx] = self.array[idx]
        self.array = new_array
    
    def _validate_index(self, idx):
        if idx < 0:
            idx += self.size
        if idx < 0 or idx >= self.size:
            raise IndexError("array index out of range")