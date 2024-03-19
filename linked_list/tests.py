from singly_linked_list import SinglyLinkedList
from doubly_linked_list import DoublyLinkedList
import unittest


class SinglyLinkedListTest(unittest.TestCase):
    def setUp(self):
        self.list = SinglyLinkedList()

    def test_append(self):
        self.list.append(1)
        self.list.append(2)
        self.list.append(3)

        self.assertEqual(self.list.head.val, 1)
        self.assertEqual(self.list.tail.val, 3)
        self.assertEqual(self.list.head.next.val, 2)
        self.assertEqual(self.list.maxlen, 3)

    def test_appendleft(self):
        self.list.appendleft(1)
        self.list.appendleft(3)
        self.list.appendleft(2)

        self.assertEqual(self.list.head.val, 2)
        self.assertEqual(self.list.tail.val, 1)
        self.assertEqual(self.list.head.next.val, 3)
        self.assertEqual(self.list.maxlen, 3)

    def test_clear(self):
        self.list.append(1)
        self.list.append(2)

        self.list.clear()

        self.assertIsNone(self.list.head)
        self.assertIsNone(self.list.tail)

    def test_copy(self):
        self.list.append(2)
        self.list.append(1)
        self.list.append(3)

        new_list = self.list.copy()

        self.assertEqual(new_list.head.val, 2)
        self.assertEqual(new_list.tail.val, 3)
        self.assertEqual(new_list.head.next.val, 1)
        self.assertEqual(new_list.maxlen, 3)

    def test_count(self):
        self.list.append(1)
        self.list.append(3)
        self.list.appendleft(2)
        self.list.appendleft(1)

        self.assertEqual(self.list.count(1), 2)

    def test_extend(self):
        self.list.append(1)
        self.list.extend([2, 3, 4])

        self.assertEqual(len(self.list), 4)
        self.assertEqual(self.list.head.val, 1)
        self.assertEqual(self.list.tail.val, 4)
    
    def test_extendleft(self):
        self.list.append(1)
        self.list.extendleft([2, 3, 4])
        # 4, 3, 2, 1

        self.assertEqual(len(self.list), 4)
        self.assertEqual(self.list.head.val, 4)
        self.assertEqual(self.list.tail.val, 1)

    def test_index(self):
        self.list.append(1)
        self.list.append(2)
        self.list.append(3)
        self.list.append(2)

        self.assertEqual(self.list.index(1), 0)
        self.assertEqual(self.list.index(2), 1)
        self.assertEqual(self.list.index(3), 2)

        with self.assertRaises(ValueError):
            self.list.index(5)

    def test_insert(self):
        self.list.append(1)
        self.list.append(2)

        self.list.insert(1, 3)
        self.assertEqual(self.list.head.next.val, 3)
        
        self.list.insert(0, 2)
        self.assertEqual(self.list.head.val, 2)
        
        self.list.insert(4, 5)
        self.assertEqual(self.list.tail.val, 5)

        self.assertEqual(len(self.list), 5)

        with self.assertRaises(IndexError):
            self.list.insert(6, 7)

    def test_pop(self):
        self.list.append(1)
        self.list.append(2)
        self.list.append(3)

        self.assertEqual(self.list.pop(), 3)
        self.assertEqual(self.list.tail.val, 2)
        self.list.pop()
        self.list.pop()

        with self.assertRaises(IndexError):
            self.list.pop()

    def test_popleft(self):
        self.list.append(1)
        self.list.append(2)
        self.list.append(3)

        self.assertEqual(self.list.popleft(), 1)
        self.assertEqual(self.list.tail.val, 3)
        self.assertEqual(self.list.head.val, 2)
        self.list.popleft()
        self.list.popleft()

        with self.assertRaises(IndexError):
            self.list.popleft()

    def test_remove(self):
        self.list.append(1)
        self.list.append(2)
        self.list.append(3)

        self.list.remove(2)
        self.assertEqual(self.list.head.val, 1)
        self.assertEqual(self.list.head.next.val, 3)
        self.assertEqual(len(self.list), 2)

        self.list.remove(1)
        self.assertEqual(self.list.head.val, 3)
        
        with self.assertRaises(ValueError):
            self.list.remove(4)

    def test_reserve(self):
        self.list.append(1)
        self.list.append(2)
        self.list.append(3)

        self.list.reverse()
        self.assertEqual(self.list.head.val, 3)
        self.assertEqual(self.list.tail.val, 1)
        self.assertEqual(self.list.head.next.val, 2)

    def test_rotate(self):
        self.list.append(1)
        self.list.append(2)
        self.list.append(3)
        self.list.append(4)

        self.list.rotate(1)
        self.assertEqual(self.list.head.val, 4)
        self.assertEqual(self.list.tail.val, 3)

        self.list.rotate(2)
        self.assertEqual(self.list.head.val, 2)
        self.assertEqual(self.list.tail.val, 1)

        self.list.rotate(-1)
        self.assertEqual(self.list.head.val, 3)
        self.assertEqual(self.list.tail.val, 2)


class DoublyLinkedListTest(unittest.TestCase):
    def setUp(self):
        self.list = DoublyLinkedList()

    def test_append(self):
        self.list.append(1)
        self.list.append(2)
        self.list.append(3)

        self.assertEqual(self.list.head.val, 1)
        self.assertEqual(self.list.tail.val, 3)
        self.assertEqual(self.list.head.next.val, 2)
        self.assertEqual(self.list.maxlen, 3)

    def test_appendleft(self):
        self.list.appendleft(1)
        self.list.appendleft(3)
        self.list.appendleft(2)

        self.assertEqual(self.list.head.val, 2)
        self.assertEqual(self.list.tail.val, 1)
        self.assertEqual(self.list.head.next.val, 3)
        self.assertEqual(self.list.maxlen, 3)

    def test_clear(self):
        self.list.append(1)
        self.list.append(2)

        self.list.clear()

        self.assertIsNone(self.list.head)
        self.assertIsNone(self.list.tail)

    def test_copy(self):
        self.list.append(2)
        self.list.append(1)
        self.list.append(3)

        new_list = self.list.copy()

        self.assertEqual(new_list.head.val, 2)
        self.assertEqual(new_list.tail.val, 3)
        self.assertEqual(new_list.head.next.val, 1)
        self.assertEqual(new_list.maxlen, 3)

    def test_count(self):
        self.list.append(1)
        self.list.append(3)
        self.list.appendleft(2)
        self.list.appendleft(1)

        self.assertEqual(self.list.count(1), 2)

    def test_extend(self):
        self.list.append(1)
        self.list.extend([2, 3, 4])

        self.assertEqual(len(self.list), 4)
        self.assertEqual(self.list.head.val, 1)
        self.assertEqual(self.list.tail.val, 4)
    
    def test_extendleft(self):
        self.list.append(1)
        self.list.extendleft([2, 3, 4])
        # 4, 3, 2, 1

        self.assertEqual(len(self.list), 4)
        self.assertEqual(self.list.head.val, 4)
        self.assertEqual(self.list.tail.val, 1)

    def test_index(self):
        self.list.append(1)
        self.list.append(2)
        self.list.append(3)
        self.list.append(2)

        self.assertEqual(self.list.index(1), 0)
        self.assertEqual(self.list.index(2), 1)
        self.assertEqual(self.list.index(3), 2)

        with self.assertRaises(ValueError):
            self.list.index(5)

    def test_insert(self):
        self.list.append(1)
        self.list.append(2)

        self.list.insert(1, 3)
        self.assertEqual(self.list.head.next.val, 3)
        
        self.list.insert(0, 2)
        self.assertEqual(self.list.head.val, 2)
        
        self.list.insert(4, 5)
        self.assertEqual(self.list.tail.val, 5)

        self.assertEqual(len(self.list), 5)

        with self.assertRaises(IndexError):
            self.list.insert(6, 7)

    def test_pop(self):
        self.list.append(1)
        self.list.append(2)
        self.list.append(3)

        self.assertEqual(self.list.pop(), 3)
        self.assertEqual(self.list.tail.val, 2)
        self.list.pop()
        self.list.pop()

        with self.assertRaises(IndexError):
            self.list.pop()

    def test_popleft(self):
        self.list.append(1)
        self.list.append(2)
        self.list.append(3)

        self.assertEqual(self.list.popleft(), 1)
        self.assertEqual(self.list.tail.val, 3)
        self.assertEqual(self.list.head.val, 2)
        self.list.popleft()
        self.list.popleft()

        with self.assertRaises(IndexError):
            self.list.popleft()

    def test_remove(self):
        self.list.append(1)
        self.list.append(2)
        self.list.append(3)

        self.list.remove(2)
        self.assertEqual(self.list.head.val, 1)
        self.assertEqual(self.list.head.next.val, 3)
        self.assertEqual(len(self.list), 2)

        self.list.remove(1)
        self.assertEqual(self.list.head.val, 3)
        
        with self.assertRaises(ValueError):
            self.list.remove(4)

    def test_reserve(self):
        self.list.append(1)
        self.list.append(2)
        self.list.append(3)

        self.list.reverse()
        self.assertEqual(self.list.head.val, 3)
        self.assertEqual(self.list.tail.val, 1)
        self.assertEqual(self.list.head.next.val, 2)

    def test_rotate(self):
        self.list.append(1)
        self.list.append(2)
        self.list.append(3)
        self.list.append(4)

        self.list.rotate(1)
        self.assertEqual(self.list.head.val, 4)
        self.assertEqual(self.list.tail.val, 3)

        self.list.rotate(2)
        self.assertEqual(self.list.head.val, 2)
        self.assertEqual(self.list.tail.val, 1)

        self.list.rotate(-1)
        self.assertEqual(self.list.head.val, 3)
        self.assertEqual(self.list.tail.val, 2)


if __name__ == '__main__':
    unittest.main()