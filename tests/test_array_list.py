from array_list.dynamic_array import ArrayList
import unittest


class ArrayListTest(unittest.TestCase):
    def setUp(self):
        self.array = ArrayList()
    
    def test_append(self):
        self.array.append(1)
        self.assertEqual(self.array[0], 1)
        self.array.append(2)
        self.assertEqual(self.array[-1], 2)
        self.assertEqual(len(self.array), 2)
    
    def test_extend(self):
        self.array.extend([1, 2])
        self.assertEqual(self.array[0], 1)
        self.array.extend([3, 2])
        self.assertEqual(len(self.array), 4)
    
    def test_insert(self):
        self.array.insert(0, 1)
        self.array.insert(0, 2)
        self.array.insert(0, 3)
        self.array.insert(3, 4)
        self.assertEqual(len(self.array), 4)
        self.assertEqual(self.array[-1], 4)

        with self.assertRaises(IndexError):
            self.array.insert(5, 0)

    def test_remove(self):
        self.array.append(1)
        self.array.append(2)
        self.array.append(3)

        self.array.remove(2)
        self.assertEqual(len(self.array), 2)
        self.assertEqual(self.array[0], 1)
        self.assertEqual(self.array[1], 3)

        with self.assertRaises(ValueError):
            self.array.remove(5)
    
    def test_pop(self):
        self.array.append(1)
        self.array.append(2)
        self.array.append(3)

        item = self.array.pop()
        self.assertEqual(item, 3)
        item = self.array.pop(0)
        self.assertEqual(item, 1)
        self.assertEqual(len(self.array), 1)

        with self.assertRaises(IndexError):
            self.array.pop(3)

        self.array.pop()
        with self.assertRaises(IndexError):
            self.array.pop()


    def test_clear(self):
        self.array.append(1)
        self.array.append(2)
        self.array.append(3)

        self.array.clear()
        self.assertEqual(len(self.array), 0)

    def test_index(self):
        self.array.append(1)
        self.array.append(2)
        self.array.append(3)

        idx = self.array.index(2)
        self.assertEqual(idx, 1)
        idx = self.array.index(3)
        self.assertEqual(idx, 2)
        with self.assertRaises(ValueError):
            self.array.index(5)

    def test_count(self):
        self.array.append(1)
        self.array.append(2)
        self.array.append(3)

        self.assertEqual(self.array.count(2), 1)

        self.array.append(2)
        self.assertEqual(self.array.count(2), 2)

    def test_sort(self):
        self.array.append(1)
        self.array.append(3)
        self.array.append(2)

        self.array.sort()
        self.assertListEqual(self.array.to_list(), [1, 2, 3])
    
    def test_reverse(self):
        self.array.append(1)
        self.array.append(2)
        self.array.append(3)

        self.array.reverse()
        self.assertListEqual(self.array.to_list(), [3, 2, 1])
    
    def test_copy(self):
        self.array.append(1)
        self.array.append(2)
        self.array.append(3)

        new_array = self.array.copy()
        self.assertListEqual(self.array.to_list(), new_array)


if __name__ == '__main__':
    unittest.main()