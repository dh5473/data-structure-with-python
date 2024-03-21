from queue_with_two_stacks import QueueWithStack
from circular_queue import CircularQueue
from linked_queue import LinkedQueue
import unittest


class LinkedQueueTest(unittest.TestCase):
    def setUp(self):
        self.queue = LinkedQueue()

    def test_enqueue(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)

        self.assertEqual(self.queue.head.val, 1)
        self.assertEqual(self.queue.tail.val, 3)
        
        self.queue.dequeue()
        self.assertEqual(self.queue.head.val, 2)

        self.queue.enqueue(4)
        self.assertEqual(self.queue.tail.val, 4)

    def test_dequeue(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)

        self.assertEqual(self.queue.dequeue(), 1)
        self.assertEqual(self.queue.dequeue(), 2)
        self.assertEqual(self.queue.head.val, 3)

        self.queue.dequeue()
        with self.assertRaises(IndexError):
            self.queue.dequeue()

    def test_peek(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)

        self.assertEqual(self.queue.peek(), 1)
        self.assertEqual(self.queue.peek(), 1)
        
        self.assertEqual(self.queue.dequeue(), 1)
        self.assertEqual(self.queue.peek(), 2)

        self.queue.dequeue()
        with self.assertRaises(ValueError):
            self.queue.peek()

    def test_size(self):
        self.assertEqual(self.queue.size(), 0)

        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.assertEqual(self.queue.size(), 2)
        
        self.queue.dequeue()
        self.assertEqual(self.queue.size(), 1)

        self.queue.dequeue()
        self.assertEqual(self.queue.size(), 0)        

    def test_is_empty(self):
        self.assertEqual(self.queue.is_empty(), True)
        
        self.queue.enqueue(1)
        self.assertEqual(self.queue.is_empty(), False)

        self.queue.dequeue()
        self.assertEqual(self.queue.is_empty(), True)


class QueueWithStackTest(unittest.TestCase):
    def setUp(self):
        self.queue = QueueWithStack()
    
    def test_enqueue(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)

        self.assertListEqual(self.queue.stack_in, [1, 2, 3])

        self.queue.dequeue()
        self.assertListEqual(self.queue.stack_in, [])
        self.assertListEqual(self.queue.stack_out, [3, 2])

        self.queue.enqueue(4)
        self.assertListEqual(self.queue.stack_in, [4])
        self.assertListEqual(self.queue.stack_out, [3, 2])

    def test_dequeue(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)

        self.assertListEqual(self.queue.stack_in, [1, 2, 3])

        self.assertEqual(self.queue.dequeue(), 1)
        self.assertListEqual(self.queue.stack_in, [])
        self.assertListEqual(self.queue.stack_out, [3, 2])

        self.queue.enqueue(4)
        self.assertListEqual(self.queue.stack_in, [4])
        self.assertListEqual(self.queue.stack_out, [3, 2])
        self.assertEqual(self.queue.dequeue(), 2)
        self.assertEqual(self.queue.dequeue(), 3)
        self.assertEqual(self.queue.dequeue(), 4)

        with self.assertRaises(IndexError):
            self.queue.dequeue()

    def test_peek(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)

        self.assertEqual(self.queue.peek(), 1)
        self.assertEqual(self.queue.peek(), 1)
        
        self.assertEqual(self.queue.dequeue(), 1)
        self.assertEqual(self.queue.peek(), 2)

        self.queue.dequeue()
        with self.assertRaises(ValueError):
            self.queue.peek()

    def test_size(self):
        self.assertEqual(self.queue.size(), 0)

        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.assertEqual(self.queue.size(), 2)
        
        self.queue.dequeue()
        self.assertEqual(self.queue.size(), 1)

        self.queue.dequeue()
        self.assertEqual(self.queue.size(), 0)        

    def test_is_empty(self):
        self.assertEqual(self.queue.is_empty(), True)
        
        self.queue.enqueue(1)
        self.assertEqual(self.queue.is_empty(), False)

        self.queue.dequeue()
        self.assertEqual(self.queue.is_empty(), True)


class CircularQueueTest(unittest.TestCase):
    def setUp(self):
        self.queue = CircularQueue()

    def test_enqueue(self):
        pass

    def test_dequeue(self):
        pass

    def test_front(self):
        pass

    def test_rear(self):
        pass

    def test_is_empty(self):
        pass

    def test_is_full(self):
        pass


if __name__ == '__main__':
    unittest.main()