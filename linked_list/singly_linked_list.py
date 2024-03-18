class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.maxlen = 0
    
    def __len__(self):
        return self.maxlen

    def append(self, item):
        node = Node(item)

        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

        self.maxlen += 1

    def appendleft(self, item):
        node = Node(item)

        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node

        self.maxlen += 1

    def clear(self):
        self.head = None
        self.tail = None
        self.maxlen = 0

    def copy(self):
        ret_list = SinglyLinkedList()
        curr_node = self.head
        while curr_node:
            ret_list.append(curr_node.val)
            curr_node = curr_node.next

        return ret_list

    def count(self, item):
        cnt = 0
        curr_node = self.head
        while curr_node:
            if curr_node.val == item:
                cnt += 1
            curr_node = curr_node.next
        return cnt
    
    def extend(self, iterable):
        for item in iterable:
            self.append(item)
            self.maxlen += 1

    def extendleft(self, iterable):
        for item in iterable:
            self.appendleft(item)
            self.maxlen += 1

    def index(self, item):
        idx = 0
        curr_node = self.head
        while curr_node:
            if curr_node.val == item:
                return idx
            idx += 1
            curr_node = curr_node.next
        else:
            raise ValueError(f"{item} is not in linked list")

    def insert(self, i, item):
        if self.maxlen < i:
            raise IndexError("index out of range")

        if i == 0:
            self.appendleft(item)
        else:
            idx = 0
            curr_node = self.head
            node = Node(item)
            while curr_node:
                if idx + 1 == i:
                    next_node = curr_node.next
                    curr_node.next = node
                    node.next = next_node
                    break
                idx += 1
                curr_node = curr_node.next
            self.maxlen += 1

    def pop(self):
        if not self.head:
            raise IndexError("pop for empty linked list")
        
        curr_node = self.head
        ret_node_val = self.tail.val
        while curr_node:
            if curr_node.next == self.tail:
                self.tail = curr_node
                self.maxlen -= 1
                return ret_node_val
            
            curr_node = curr_node.next

    def popleft(self):
        if not self.head:
            raise IndexError("popleft for empty linked list")
        
        ret_node_val = self.head.val
        self.head = self.head.next
        self.maxlen -= 1

        return ret_node_val
    
    def remove(self, item):
        curr_node = self.head
        while curr_node:
            if curr_node.next.val == item:
                curr_node.next = curr_node.next.next
                self.maxlen -= 1
                break
        else:
            raise ValueError("list.remove(x): x not in linked list")

    # 수정 필요
    def reverse(self):
        curr_node = self.head
        self.tail = curr_node
        while curr_node:
            next_node = curr_node.next
            next_node.next = curr_node
            curr_node = next_node
            if not next_node:
                self.head = curr_node

    def rotate(self, n=1):
        if n > 0:
            for _ in range(n):
                self.appendleft(self.pop())
        else:
            for _ in range(-n):
                self.append(self.popleft())

    def to_list(self):
        ret_list = []
        curr_node = self.head
        while curr_node:
            ret_list.append(curr_node.val)
            curr_node = curr_node.next

        return ret_list

    def print_val(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.val)
            curr_node = curr_node.next