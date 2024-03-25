import hash_table_with_separate_chaining as sc
import hash_table_with_linear_probing as lp
import hash_table_with_quadratic_probing as qp
import hash_table_with_double_hashing as dh
import unittest


class SeparateChainingHashTableTest(unittest.TestCase):
    def setUp(self):
        self.table = sc.HashTable()

    def test_insert(self):
        self.table.insert('a', 1)
        self.table.insert('b', 2)
        self.assertEqual(self.table.search('a'), 1)
        self.assertEqual(self.table.search('b'), 2)
        self.assertEqual(self.table.size, 2)

        self.table.insert('a', 3)
        self.table.insert('c', 'cc')
        self.assertEqual(self.table.search('a'), 3)
        self.assertEqual(self.table.search('c'), 'cc')
        self.assertEqual(self.table.size, 3)

        self.table.insert(1, 3)
        self.table.insert(2, 'a')
        self.assertEqual(self.table.search(1), 3)
        self.assertEqual(self.table.search(2), 'a')
        self.assertEqual(self.table.size, 5)

        self.table.insert((3, 4), 2)
        self.table.insert(('a', 'b'), 'ab')
        self.assertEqual(self.table.search((3, 4)), 2)
        self.assertEqual(self.table.search(('a', 'b')), 'ab')
        self.assertEqual(self.table.size, 7)

    def test_search(self):
        self.table.insert('a', 1)
        self.table.insert('b', 2)
        self.assertEqual(self.table.search('a'), 1)
        self.assertEqual(self.table.search('b'), 2)
        self.assertEqual(self.table.size, 2)

        self.table.insert('a', 3)
        self.table.insert('c', 'cc')
        self.assertEqual(self.table.search('a'), 3)
        self.assertEqual(self.table.search('c'), 'cc')
        self.assertEqual(self.table.size, 3)

        self.table.insert(1, 3)
        self.table.insert(2, 'a')
        self.assertEqual(self.table.search(1), 3)
        self.assertEqual(self.table.search(2), 'a')
        self.assertEqual(self.table.size, 5)

        self.table.insert((3, 4), 2)
        self.table.insert(('a', 'b'), 'ab')
        self.assertEqual(self.table.search((3, 4)), 2)
        self.assertEqual(self.table.search(('a', 'b')), 'ab')
        self.assertEqual(self.table.size, 7)

        with self.assertRaises(KeyError):
            self.table.search(5)

        with self.assertRaises(KeyError):
            self.table.search('1')
        
        with self.assertRaises(KeyError):
            self.table.search('d')

    def test_remove(self):
        self.table.insert('a', 1)
        self.table.insert('b', 2)
        self.assertEqual(self.table.search('a'), 1)
        self.assertEqual(self.table.search('b'), 2)
        self.assertEqual(self.table.size, 2)

        self.table.insert('a', 3)
        self.table.insert('c', 'cc')
        self.assertEqual(self.table.search('a'), 3)
        self.assertEqual(self.table.search('c'), 'cc')
        self.assertEqual(self.table.size, 3)

        self.table.remove('a')
        self.assertEqual(self.table.size, 2)
        with self.assertRaises(KeyError):
            self.table.search('a')

        self.table.insert(1, 3)
        self.table.insert(2, 'a')
        self.assertEqual(self.table.search(1), 3)
        self.assertEqual(self.table.search(2), 'a')
        self.assertEqual(self.table.size, 4)

        self.table.remove(1)
        self.assertEqual(self.table.size, 3)
        with self.assertRaises(KeyError):
            self.table.search(1)
        
        
        self.table.insert((3, 4), 2)
        self.table.insert(('a', 'b'), 'ab')
        self.assertEqual(self.table.search((3, 4)), 2)
        self.assertEqual(self.table.search(('a', 'b')), 'ab')
        self.assertEqual(self.table.size, 5)

        self.table.remove((3, 4))
        self.assertEqual(self.table.size, 4)
        with self.assertRaises(KeyError):
            self.table.search((3, 4))

    def test_rehash(self):
        self.table.insert('a', 1)
        self.table.insert('b', 2)
        self.assertEqual(self.table.size, 2)
        self.assertEqual(self.table.capacity, 4)

        self.table.insert(1, 2)
        self.table.insert(2, 3)
        self.assertEqual(self.table.size, 4)
        self.assertEqual(self.table.capacity, 8)

        self.table.insert(3, 3)
        self.table.insert(4, 4)
        self.table.insert(5, 5)
        self.assertEqual(self.table.size, 7)
        self.assertEqual(self.table.capacity, 16)


class LinearProbingHashTableTest(unittest.TestCase):
    def setUp(self):
        self.table = lp.HashTable()

    def test_insert(self):
        self.table.insert('a', 1)
        self.table.insert('b', 2)
        self.assertEqual(self.table.search('a'), 1)
        self.assertEqual(self.table.search('b'), 2)
        self.assertEqual(self.table.size, 2)

        self.table.insert('a', 3)
        self.table.insert('c', 'cc')
        self.assertEqual(self.table.search('a'), 3)
        self.assertEqual(self.table.search('c'), 'cc')
        self.assertEqual(self.table.size, 3)

        self.table.insert(1, 3)
        self.table.insert(2, 'a')
        self.assertEqual(self.table.search(1), 3)
        self.assertEqual(self.table.search(2), 'a')
        self.assertEqual(self.table.size, 5)

        self.table.insert((3, 4), 2)
        self.table.insert(('a', 'b'), 'ab')
        self.assertEqual(self.table.search((3, 4)), 2)
        self.assertEqual(self.table.search(('a', 'b')), 'ab')
        self.assertEqual(self.table.size, 7)

    def test_search(self):
        self.table.insert('a', 1)
        self.table.insert('b', 2)
        self.assertEqual(self.table.search('a'), 1)
        self.assertEqual(self.table.search('b'), 2)
        self.assertEqual(self.table.size, 2)

        self.table.insert('a', 3)
        self.table.insert('c', 'cc')
        self.assertEqual(self.table.search('a'), 3)
        self.assertEqual(self.table.search('c'), 'cc')
        self.assertEqual(self.table.size, 3)

        self.table.insert(1, 3)
        self.table.insert(2, 'a')
        self.assertEqual(self.table.search(1), 3)
        self.assertEqual(self.table.search(2), 'a')
        self.assertEqual(self.table.size, 5)

        self.table.insert((3, 4), 2)
        self.table.insert(('a', 'b'), 'ab')
        self.assertEqual(self.table.search((3, 4)), 2)
        self.assertEqual(self.table.search(('a', 'b')), 'ab')
        self.assertEqual(self.table.size, 7)

        with self.assertRaises(KeyError):
            self.table.search(5)

        with self.assertRaises(KeyError):
            self.table.search('1')
        
        with self.assertRaises(KeyError):
            self.table.search('d')

    def test_remove(self):
        self.table.insert('a', 1)
        self.table.insert('b', 2)
        self.assertEqual(self.table.search('a'), 1)
        self.assertEqual(self.table.search('b'), 2)
        self.assertEqual(self.table.size, 2)

        self.table.insert('a', 3)
        self.table.insert('c', 'cc')
        self.assertEqual(self.table.search('a'), 3)
        self.assertEqual(self.table.search('c'), 'cc')
        self.assertEqual(self.table.size, 3)

        self.table.remove('a')
        self.assertEqual(self.table.size, 2)
        with self.assertRaises(KeyError):
            self.table.search('a')

        self.table.insert(1, 3)
        self.table.insert(2, 'a')
        self.assertEqual(self.table.search(1), 3)
        self.assertEqual(self.table.search(2), 'a')
        self.assertEqual(self.table.size, 4)

        self.table.remove(1)
        self.assertEqual(self.table.size, 3)
        with self.assertRaises(KeyError):
            self.table.search(1)
        
        
        self.table.insert((3, 4), 2)
        self.table.insert(('a', 'b'), 'ab')
        self.assertEqual(self.table.search((3, 4)), 2)
        self.assertEqual(self.table.search(('a', 'b')), 'ab')
        self.assertEqual(self.table.size, 5)

        self.table.remove((3, 4))
        self.assertEqual(self.table.size, 4)
        with self.assertRaises(KeyError):
            self.table.search((3, 4))

    def test_rehash(self):
        self.table.insert('a', 1)
        self.table.insert('b', 2)
        self.assertEqual(self.table.size, 2)
        self.assertEqual(self.table.capacity, 4)

        self.table.insert(1, 2)
        self.table.insert(2, 3)
        self.assertEqual(self.table.size, 4)
        self.assertEqual(self.table.capacity, 8)

        self.table.insert(3, 3)
        self.table.insert(4, 4)
        self.table.insert(5, 5)
        self.assertEqual(self.table.size, 7)
        self.assertEqual(self.table.capacity, 16)


class QuadraticProbingHashTableTest(unittest.TestCase):
    def setUp(self):
        self.table = qp.HashTable()

    def test_insert(self):
        self.table.insert('a', 1)
        self.table.insert('b', 2)
        self.assertEqual(self.table.search('a'), 1)
        self.assertEqual(self.table.search('b'), 2)
        self.assertEqual(self.table.size, 2)

        self.table.insert('a', 3)
        self.table.insert('c', 'cc')
        self.assertEqual(self.table.search('a'), 3)
        self.assertEqual(self.table.search('c'), 'cc')
        self.assertEqual(self.table.size, 3)

        self.table.insert(1, 3)
        self.table.insert(2, 'a')
        self.assertEqual(self.table.search(1), 3)
        self.assertEqual(self.table.search(2), 'a')
        self.assertEqual(self.table.size, 5)

        self.table.insert((3, 4), 2)
        self.table.insert(('a', 'b'), 'ab')
        self.assertEqual(self.table.search((3, 4)), 2)
        self.assertEqual(self.table.search(('a', 'b')), 'ab')
        self.assertEqual(self.table.size, 7)

    def test_search(self):
        self.table.insert('a', 1)
        self.table.insert('b', 2)
        self.assertEqual(self.table.search('a'), 1)
        self.assertEqual(self.table.search('b'), 2)
        self.assertEqual(self.table.size, 2)

        self.table.insert('a', 3)
        self.table.insert('c', 'cc')
        self.assertEqual(self.table.search('a'), 3)
        self.assertEqual(self.table.search('c'), 'cc')
        self.assertEqual(self.table.size, 3)

        self.table.insert(1, 3)
        self.table.insert(2, 'a')
        self.assertEqual(self.table.search(1), 3)
        self.assertEqual(self.table.search(2), 'a')
        self.assertEqual(self.table.size, 5)

        self.table.insert((3, 4), 2)
        self.table.insert(('a', 'b'), 'ab')
        self.assertEqual(self.table.search((3, 4)), 2)
        self.assertEqual(self.table.search(('a', 'b')), 'ab')
        self.assertEqual(self.table.size, 7)

        with self.assertRaises(KeyError):
            self.table.search(5)

        with self.assertRaises(KeyError):
            self.table.search('1')
        
        with self.assertRaises(KeyError):
            self.table.search('d')

    def test_remove(self):
        self.table.insert('a', 1)
        self.table.insert('b', 2)
        self.assertEqual(self.table.search('a'), 1)
        self.assertEqual(self.table.search('b'), 2)
        self.assertEqual(self.table.size, 2)

        self.table.insert('a', 3)
        self.table.insert('c', 'cc')
        self.assertEqual(self.table.search('a'), 3)
        self.assertEqual(self.table.search('c'), 'cc')
        self.assertEqual(self.table.size, 3)

        self.table.remove('a')
        self.assertEqual(self.table.size, 2)
        with self.assertRaises(KeyError):
            self.table.search('a')

        self.table.insert(1, 3)
        self.table.insert(2, 'a')
        self.assertEqual(self.table.search(1), 3)
        self.assertEqual(self.table.search(2), 'a')
        self.assertEqual(self.table.size, 4)

        self.table.remove(1)
        self.assertEqual(self.table.size, 3)
        with self.assertRaises(KeyError):
            self.table.search(1)
        
        
        self.table.insert((3, 4), 2)
        self.table.insert(('a', 'b'), 'ab')
        self.assertEqual(self.table.search((3, 4)), 2)
        self.assertEqual(self.table.search(('a', 'b')), 'ab')
        self.assertEqual(self.table.size, 5)

        self.table.remove((3, 4))
        self.assertEqual(self.table.size, 4)
        with self.assertRaises(KeyError):
            self.table.search((3, 4))

    def test_rehash(self):
        self.table.insert('a', 1)
        self.table.insert('b', 2)
        self.assertEqual(self.table.size, 2)
        self.assertEqual(self.table.capacity, 4)

        self.table.insert(1, 2)
        self.table.insert(2, 3)
        self.assertEqual(self.table.size, 4)
        self.assertEqual(self.table.capacity, 8)

        self.table.insert(3, 3)
        self.table.insert(4, 4)
        self.table.insert(5, 5)
        self.assertEqual(self.table.size, 7)
        self.assertEqual(self.table.capacity, 16)


class DoubleHashingHashTableTest(unittest.TestCase):
    def setUp(self):
        self.table = dh.HashTable()

    def test_insert(self):
        self.table.insert('a', 1)
        self.table.insert('b', 2)
        self.assertEqual(self.table.search('a'), 1)
        self.assertEqual(self.table.search('b'), 2)
        self.assertEqual(self.table.size, 2)

        self.table.insert('a', 3)
        self.table.insert('c', 'cc')
        self.assertEqual(self.table.search('a'), 3)
        self.assertEqual(self.table.search('c'), 'cc')
        self.assertEqual(self.table.size, 3)

        self.table.insert(1, 3)
        self.table.insert(2, 'a')
        self.assertEqual(self.table.search(1), 3)
        self.assertEqual(self.table.search(2), 'a')
        self.assertEqual(self.table.size, 5)

        self.table.insert((3, 4), 2)
        self.table.insert(('a', 'b'), 'ab')
        self.assertEqual(self.table.search((3, 4)), 2)
        self.assertEqual(self.table.search(('a', 'b')), 'ab')
        self.assertEqual(self.table.size, 7)

    def test_search(self):
        self.table.insert('a', 1)
        self.table.insert('b', 2)
        self.assertEqual(self.table.search('a'), 1)
        self.assertEqual(self.table.search('b'), 2)
        self.assertEqual(self.table.size, 2)

        self.table.insert('a', 3)
        self.table.insert('c', 'cc')
        self.assertEqual(self.table.search('a'), 3)
        self.assertEqual(self.table.search('c'), 'cc')
        self.assertEqual(self.table.size, 3)

        self.table.insert(1, 3)
        self.table.insert(2, 'a')
        self.assertEqual(self.table.search(1), 3)
        self.assertEqual(self.table.search(2), 'a')
        self.assertEqual(self.table.size, 5)

        self.table.insert((3, 4), 2)
        self.table.insert(('a', 'b'), 'ab')
        self.assertEqual(self.table.search((3, 4)), 2)
        self.assertEqual(self.table.search(('a', 'b')), 'ab')
        self.assertEqual(self.table.size, 7)

        with self.assertRaises(KeyError):
            self.table.search(5)

        with self.assertRaises(KeyError):
            self.table.search('1')
        
        with self.assertRaises(KeyError):
            self.table.search('d')

    def test_remove(self):
        self.table.insert('a', 1)
        self.table.insert('b', 2)
        self.assertEqual(self.table.search('a'), 1)
        self.assertEqual(self.table.search('b'), 2)
        self.assertEqual(self.table.size, 2)

        self.table.insert('a', 3)
        self.table.insert('c', 'cc')
        self.assertEqual(self.table.search('a'), 3)
        self.assertEqual(self.table.search('c'), 'cc')
        self.assertEqual(self.table.size, 3)

        self.table.remove('a')
        self.assertEqual(self.table.size, 2)
        with self.assertRaises(KeyError):
            self.table.search('a')

        self.table.insert(1, 3)
        self.table.insert(2, 'a')
        self.assertEqual(self.table.search(1), 3)
        self.assertEqual(self.table.search(2), 'a')
        self.assertEqual(self.table.size, 4)

        self.table.remove(1)
        self.assertEqual(self.table.size, 3)
        with self.assertRaises(KeyError):
            self.table.search(1)
        
        
        self.table.insert((3, 4), 2)
        self.table.insert(('a', 'b'), 'ab')
        self.assertEqual(self.table.search((3, 4)), 2)
        self.assertEqual(self.table.search(('a', 'b')), 'ab')
        self.assertEqual(self.table.size, 5)

        self.table.remove((3, 4))
        self.assertEqual(self.table.size, 4)
        with self.assertRaises(KeyError):
            self.table.search((3, 4))

    def test_rehash(self):
        self.table.insert('a', 1)
        self.table.insert('b', 2)
        self.assertEqual(self.table.size, 2)
        self.assertEqual(self.table.capacity, 4)

        self.table.insert(1, 2)
        self.table.insert(2, 3)
        self.assertEqual(self.table.size, 4)
        self.assertEqual(self.table.capacity, 8)

        self.table.insert(3, 3)
        self.table.insert(4, 4)
        self.table.insert(5, 5)
        self.assertEqual(self.table.size, 7)
        self.assertEqual(self.table.capacity, 16)


if __name__ == '__main__':
    unittest.main()