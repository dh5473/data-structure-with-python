class ArrayBinaryTree:
    def __init__(self, size):
        self.tree = [None] * (size + 1)
        self.size = size

    def __str__(self):
        elements = []
        for idx in range(self.size):
            elements.append(self.tree[idx] if self.tree[idx] else "-")
        return str("".join(elements))
    
    def __getitem__(self, idx):
        self._validate_index(idx)
        
        if self.tree[idx] is None:
            raise ValueError()
        
        return self.tree[idx]

    def set_root(self, val):
        self.tree[1] = val

    def set_left(self, idx, val):
        self._validate_index(idx)

        left_idx = self.find_left_child(idx)
        self.tree[left_idx] = val
    
    def set_right(self, idx, val):
        self._validate_index(idx)

        right_idx = self.find_right_child(idx)
        self.tree[right_idx] = val

    def find_parent(self, idx):
        self._validate_index(idx)

        if idx == 1:
            raise ValueError()

        return idx // 2

    def find_left_child(self, idx):
        self._validate_index(idx)

        if idx * 2 > self.size:
            raise IndexError()

        # if self.tree[idx * 2] is None:
        #     raise ValueError()

        return idx * 2

    def find_right_child(self, idx):
        self._validate_index(idx)

        if idx * 2 + 1 >= self.size:
            raise IndexError()
        
        # if self.tree[idx * 2 + 1] is None:
        #     raise ValueError()
        
        return idx * 2 + 1

    def find_left_sibling(self, idx):
        if not idx % 2:
            raise IndexError()
        
        self._validate_index(idx + 1)

        if self.tree[idx + 1] is None:
            raise ValueError()

        return idx + 1

    def find_right_sibling(self, idx):
        if idx % 2:
            raise IndexError()
        
        self._validate_index(idx - 1)
        
        if self.tree[idx - 1] is None:
            raise ValueError()

        return idx - 1

    def _validate_index(self, idx):
        if idx < 1 or idx > self.size:
            raise IndexError("tree index out of range")