class CircularQueue:
    def __init__(self, capacity=4):
        if not capacity:
            raise ValueError("zero capacity is not accepted")
        
        self.queue = [None] * capacity
        self.front_pointer = 0
        self.rear_pointer = 0
        self.maxlen = capacity
        self.length = 0
    
    def enqueue(self, item):
        if self.length == self.maxlen:
            raise IndexError("enqueue for full queue_")
        
        if self.length:
            self.rear_pointer = (self.rear_pointer + 1) % self.maxlen
        
        self.queue[self.rear_pointer] = item
        self.length += 1

    def dequeue(self):
        if not self.length:
            raise ValueError("dequeue for empty queue_")
        
        ret_val = self.queue[self.front_pointer]
        self.queue[self.front_pointer] = None
        self.length -= 1

        if self.length:
            self.front_pointer = (self.front_pointer + 1) % self.maxlen
        
        return ret_val

    def front(self):
        if self.queue[self.front_pointer] is None:
            raise ValueError("front for empty queue_")
        return self.queue[self.front_pointer]

    def rear(self):
        if self.queue[self.rear_pointer] is None:
            raise ValueError("rear for empty queue_")
        return self.queue[self.rear_pointer]

    def is_empty(self):
        if self.length:
            return False
        return True

    def is_full(self):
        if self.length < self.maxlen:
            return False
        return True