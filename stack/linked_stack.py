class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LinkedStack:
    def __init__(self):
        self.last = None
        self.length = 0

    def push(self, item):
        self.last = Node(item, self.last)
        self.length += 1

    def pop(self):
        if not self.length:
            raise IndexError("pop for empty stack")
        
        ret_node_val = self.last.val
        self.last = self.last.next
        self.length -= 1

        return ret_node_val

    def top(self):
        if not self.last:
            raise ValueError("pop for empty stack")
        return self.last.val

    def size(self):
        return self.length

    def is_empty(self):
        if self.length:
            return False
        return True