import hash_table_with_separate_chaining as sc
import hash_table_with_linear_probing as lp
import hash_table_with_quadratic_probing as qp
import hash_table_with_double_hashing as dh
import unittest


class SeparateChainingHashTableTest(unittest.TestCase):
    def setUp(self):
        self.table = sc.HashTable()

    def test_insert(self):
        pass

    def test_search(self):
        pass

    def test_remove(self):
        pass

    def test_rehash(self):
        pass

    def test_str(self):
        pass


class LinearProbingHashTableTest(unittest.TestCase):
    def setUp(self):
        self.table = lp.HashTable()

    def test_insert(self):
        pass

    def test_search(self):
        pass

    def test_remove(self):
        pass

    def test_rehash(self):
        pass

    def test_str(self):
        pass


class QuadraticProbingHashTableTest(unittest.TestCase):
    def setUp(self):
        self.table = qp.HashTable()

    def test_insert(self):
        pass

    def test_search(self):
        pass

    def test_remove(self):
        pass

    def test_rehash(self):
        pass

    def test_str(self):
        pass


class DoubleHashingHashTableTest(unittest.TestCase):
    def setUp(self):
        self.table = dh.HashTable()

    def test_insert(self):
        pass

    def test_search(self):
        pass

    def test_remove(self):
        pass

    def test_rehash(self):
        pass

    def test_str(self):
        pass


if __name__ == '__main__':
    unittest.main()