class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class LinkedQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def enqueue(self, item):
        node = Node(item)

        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

        self.length += 1

    def dequeue(self):
        if not self.length:
            raise IndexError()

        ret_node = self.head
        if self.head.next:
            self.head = self.head.next
        else:
            self.head = None
            self.tail = None

        self.length -= 1
        
        return ret_node.val

    def peek(self):
        if not self.head:
            raise ValueError()
        return self.head.val

    def size(self):
        return self.length
    
    def is_empty(self):
        if self.length:
            return False
        return True