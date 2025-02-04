class QueueWithStack:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []
        self.length = 0

    def enqueue(self, item):
        self.stack_in.append(item)
        self.length += 1

    def dequeue(self):
        if not self.length:
            raise IndexError("dequeue for empty queue_")

        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        
        self.length -= 1
        return self.stack_out.pop()

    def peek(self):
        if not self.length:
            raise ValueError("peek for empty queue_")

        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        
        return self.stack_out[-1]

    def size(self):
        return self.length
    
    def is_empty(self):
        if self.length:
            return False
        return True