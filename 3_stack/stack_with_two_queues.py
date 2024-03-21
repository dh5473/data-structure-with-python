from collections import deque  # just data structure with doubly linked list
# import queue -> for communication with different threads


class StackWithQueue:
    def __init__(self):
        self.q_one = deque()
        self.q_two = deque()
        self.length = 0

    def push(self, item):
        self.q_one.append(item)
        self.length += 1

    def pop(self):
        if not self.length:
            raise IndexError("pop for empty stack")

        for _ in range(self.length - 1):
            self.q_two.append(self.q_one.popleft())
        
        ret_val = self.q_one.popleft()
        self.length -= 1

        self.q_one, self.q_two = self.q_two, self.q_one

        return ret_val

    def top(self):
        if not self.length:
            raise ValueError("top for empty stack")
        return self.q_one[-1]

    def size(self):
        return self.length

    def is_empty(self):
        if self.length:
            return False
        return True