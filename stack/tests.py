from stack_with_two_queues import StackWithQueue
from linked_stack import LinkedStack
import unittest


class LinkedStackTest(unittest.TestCase):
    def setUp(self):
        self.stack = LinkedStack()

    def test_push(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)

        self.assertEqual(self.stack.pop(), 3)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.last.val, 1)

        self.stack.push(4)
        self.assertEqual(self.stack.pop(), 4)
        self.assertEqual(self.stack.pop(), 1)

    def test_pop(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)

        self.assertEqual(self.stack.pop(), 3)
        self.assertEqual(self.stack.pop(), 2)

        self.stack.push(4)
        self.assertEqual(self.stack.pop(), 4)
        self.assertEqual(self.stack.pop(), 1)

        with self.assertRaises(IndexError):
            self.stack.pop()

    def test_top(self):
        self.stack.push(1)
        self.stack.push(2)

        self.assertEqual(self.stack.top(), 2)
        self.assertEqual(self.stack.top(), 2)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.top(), 1)
        self.stack.pop()

        with self.assertRaises(ValueError):
            self.stack.top()

    def test_size(self):
        self.stack.push(1)
        self.assertEqual(self.stack.size(), 1)
        
        self.stack.push(2)
        self.assertEqual(self.stack.size(), 2)

        self.stack.pop()
        self.stack.pop()
        self.assertEqual(self.stack.size(), 0)

    def test_is_empty(self):
        self.assertEqual(self.stack.is_empty(), 1)

        self.stack.push(1)
        self.assertEqual(self.stack.is_empty(), 0)

        self.stack.pop()
        self.assertEqual(self.stack.is_empty(), 1)


class StackWithQueueTest(unittest.TestCase):
    def setUp(self):
        self.stack = StackWithQueue()

    def test_push(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)

        self.assertEqual(self.stack.pop(), 3)
        self.assertEqual(self.stack.pop(), 2)

        self.stack.push(4)
        self.assertEqual(self.stack.pop(), 4)
        self.assertEqual(self.stack.pop(), 1)

    def test_pop(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)

        self.assertEqual(self.stack.pop(), 3)
        self.assertEqual(self.stack.pop(), 2)

        self.stack.push(4)
        self.assertEqual(self.stack.pop(), 4)
        self.assertEqual(self.stack.pop(), 1)

        with self.assertRaises(IndexError):
            self.stack.pop()

    def test_top(self):
        self.stack.push(1)
        self.stack.push(2)

        self.assertEqual(self.stack.top(), 2)
        self.assertEqual(self.stack.top(), 2)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.top(), 1)
        self.stack.pop()

        with self.assertRaises(ValueError):
            self.stack.top()

    def test_size(self):
        self.stack.push(1)
        self.assertEqual(self.stack.size(), 1)
        
        self.stack.push(2)
        self.assertEqual(self.stack.size(), 2)

        self.stack.pop()
        self.stack.pop()
        self.assertEqual(self.stack.size(), 0)

    def test_is_empty(self):
        self.assertEqual(self.stack.is_empty(), 1)

        self.stack.push(1)
        self.assertEqual(self.stack.is_empty(), 0)

        self.stack.pop()
        self.assertEqual(self.stack.is_empty(), 1)


if __name__ == '__main__':
    unittest.main()