import graph.adjacency_matrix_graph as mg
import graph.adjacency_list_graph as lg
import unittest


class MatrixUndirectedGraphTest(unittest.TestCase):
    def setUp(self):
        self.graph = mg.UndirectedGraph(4)
    
    def test_add_edge(self):
        self.graph.add_edge(0, 1)
        self.graph.add_edge(2, 1)
        self.graph.add_edge(1, 3, 2)

        self.assertEqual(self.graph.matrix[0][1], 1)
        self.assertEqual(self.graph.matrix[1][0], 1)
        self.assertEqual(self.graph.matrix[1][2], 1)
        self.assertEqual(self.graph.matrix[2][1], 1)
        self.assertEqual(self.graph.matrix[1][3], 2)
        self.assertEqual(self.graph.matrix[3][1], 2)

        with self.assertRaises(IndexError):
            self.graph.add_edge(4, 2)
        
        with self.assertRaises(ValueError):
            self.graph.add_edge(2, 2)

    def test_remove_edge(self):
        self.graph.add_edge(0, 1)
        self.graph.add_edge(2, 1)
        self.graph.add_edge(1, 3, 2)
        
        self.graph.remove_edge(0, 1)
        self.assertEqual(self.graph.matrix[0][1], 0)
        self.assertEqual(self.graph.matrix[1][0], 0)

        self.assertEqual(self.graph.matrix[1][2], 1)
        self.assertEqual(self.graph.matrix[2][1], 1)
        self.assertEqual(self.graph.matrix[1][3], 2)
        self.assertEqual(self.graph.matrix[3][1], 2)

        self.graph.remove_edge(1, 3)
        self.assertEqual(self.graph.matrix[3][1], 0)
        self.assertEqual(self.graph.matrix[1][3], 0)

        with self.assertRaises(IndexError):
            self.graph.remove_edge(1, 4)
        
        with self.assertRaises(ValueError):
            self.graph.remove_edge(2, 2)
        
        with self.assertRaises(ValueError):
            self.graph.remove_edge(0, 2)


class MatrixDirectedGraphTest(unittest.TestCase):
    def setUp(self):
        self.graph = mg.DirectedGraph(4)

    def test_add_edge(self):
        self.graph.add_edge(0, 1)
        self.graph.add_edge(2, 1)
        self.graph.add_edge(1, 3, 2)

        self.assertEqual(self.graph.matrix[0][1], 1)
        self.assertEqual(self.graph.matrix[1][0], 0)
        self.assertEqual(self.graph.matrix[1][2], 0)
        self.assertEqual(self.graph.matrix[2][1], 1)
        self.assertEqual(self.graph.matrix[1][3], 2)
        self.assertEqual(self.graph.matrix[3][1], 0)

        self.graph.add_edge(1, 0)
        self.assertEqual(self.graph.matrix[1][0], 1)

        self.graph.add_edge(3, 1, 2)
        self.assertEqual(self.graph.matrix[3][1], 2)

        with self.assertRaises(IndexError):
            self.graph.add_edge(4, 2)
        
        with self.assertRaises(ValueError):
            self.graph.add_edge(2, 2)

    def test_remove_edge(self):
        self.graph.add_edge(0, 1)
        self.graph.add_edge(1, 0)
        self.graph.add_edge(2, 1)
        self.graph.add_edge(1, 3, 2)
        
        self.assertEqual(self.graph.matrix[0][1], 1)
        self.assertEqual(self.graph.matrix[1][0], 1)

        self.graph.remove_edge(0, 1)
        self.assertEqual(self.graph.matrix[0][1], 0)
        self.assertEqual(self.graph.matrix[1][0], 1)

        self.assertEqual(self.graph.matrix[1][2], 0)
        self.assertEqual(self.graph.matrix[2][1], 1)
        self.assertEqual(self.graph.matrix[1][3], 2)
        self.assertEqual(self.graph.matrix[3][1], 0)

        self.graph.remove_edge(1, 3)
        self.assertEqual(self.graph.matrix[1][3], 0)
        self.assertEqual(self.graph.matrix[3][1], 0)

        with self.assertRaises(IndexError):
            self.graph.remove_edge(1, 4)
        
        with self.assertRaises(ValueError):
            self.graph.remove_edge(2, 2)
        
        with self.assertRaises(ValueError):
            self.graph.remove_edge(0, 2)


class LinkedListUndirectedGraphTest(unittest.TestCase):
    def setUp(self):
        self.graph = lg.UndirectedGraph(5)

    def test_add_edge(self):
        self.graph.add_edge(0, 1)
        self.graph.add_edge(1, 2)
        self.graph.add_edge(0, 3)

        self.assertEqual(self.graph.array[0].idx, 0)
        self.assertEqual(self.graph.array[1].idx, 1)
        self.assertEqual(self.graph.array[0].next.idx, 1)
        self.assertEqual(self.graph.array[0].next.next.idx, 3)
        self.assertEqual(self.graph.array[1].next.idx, 0)
        self.assertEqual(self.graph.array[1].next.next.idx, 2)
        self.assertEqual(self.graph.array[0].next.val, 1)
        self.assertEqual(self.graph.array[1].next.val, 1)
        self.assertIsNone(self.graph.array[4])

        self.graph.add_edge(2, 3, 2)
        self.assertEqual(self.graph.array[2].next.next.idx, 3)
        self.assertEqual(self.graph.array[2].next.next.val, 2)
        self.assertEqual(self.graph.array[3].next.next.idx, 2)
        self.assertEqual(self.graph.array[3].next.next.val, 2)

        with self.assertRaises(IndexError):
            self.graph.add_edge(0, 5)
        
        with self.assertRaises(ValueError):
            self.graph.add_edge(2, 2)

    def test_remove_edge(self):
        self.graph.add_edge(0, 1)
        self.graph.add_edge(1, 2)
        self.graph.add_edge(0, 3)

        self.assertEqual(self.graph.array[0].idx, 0)
        self.assertEqual(self.graph.array[1].idx, 1)
        self.assertEqual(self.graph.array[0].next.idx, 1)
        self.assertEqual(self.graph.array[0].next.next.idx, 3)
        self.assertEqual(self.graph.array[1].next.idx, 0)
        self.assertEqual(self.graph.array[1].next.next.idx, 2)
        self.assertEqual(self.graph.array[0].next.val, 1)
        self.assertEqual(self.graph.array[1].next.val, 1)
        self.assertIsNone(self.graph.array[4])

        self.graph.add_edge(2, 3, 2)
        self.assertEqual(self.graph.array[2].next.next.idx, 3)
        self.assertEqual(self.graph.array[2].next.next.val, 2)
        self.assertEqual(self.graph.array[3].next.next.idx, 2)
        self.assertEqual(self.graph.array[3].next.next.val, 2)

        self.graph.remove_edge(1, 2)
        self.assertIsNone(self.graph.array[1].next.next)
        self.assertEqual(self.graph.array[1].next.idx, 0)
        self.assertEqual(self.graph.array[2].next.idx, 3)
        self.assertEqual(self.graph.array[2].next.val, 2)

        self.graph.remove_edge(2, 3)
        self.assertIsNone(self.graph.array[2].next)
        self.assertIsNone(self.graph.array[3].next.next)
        self.assertEqual(self.graph.array[3].next.idx, 0)
        self.assertEqual(self.graph.array[3].next.val, 1)

        with self.assertRaises(IndexError):
            self.graph.remove_edge(0, 5)
        
        with self.assertRaises(ValueError):
            self.graph.remove_edge(2, 2)

        with self.assertRaises(ValueError):
            self.graph.remove_edge(2, 3)
        
        with self.assertRaises(ValueError):
            self.graph.remove_edge(3, 2)


class LinkedListDirectedGraphTest(unittest.TestCase):
    def setUp(self):
        self.graph = lg.DirectedGraph(5)

    def test_add_edge(self):
        self.graph.add_edge(0, 1)
        self.graph.add_edge(1, 2)
        self.graph.add_edge(0, 3)

        self.assertEqual(self.graph.array[0].idx, 0)
        self.assertEqual(self.graph.array[1].idx, 1)
        self.assertEqual(self.graph.array[0].next.idx, 1)
        self.assertEqual(self.graph.array[0].next.next.idx, 3)
        self.assertEqual(self.graph.array[1].next.idx, 2)
        self.assertIsNone(self.graph.array[1].next.next)
        self.assertEqual(self.graph.array[0].next.val, 1)
        self.assertEqual(self.graph.array[1].next.val, 1)
        self.assertIsNone(self.graph.array[2])
        self.assertIsNone(self.graph.array[3])
        self.assertIsNone(self.graph.array[4])

        self.graph.add_edge(2, 3, 2)
        self.assertEqual(self.graph.array[2].next.idx, 3)
        self.assertEqual(self.graph.array[2].next.val, 2)
        self.assertIsNone(self.graph.array[3])

        with self.assertRaises(IndexError):
            self.graph.add_edge(0, 5)
        
        with self.assertRaises(ValueError):
            self.graph.add_edge(2, 2)

    def test_remove_edge(self):
        self.graph.add_edge(0, 1)
        self.graph.add_edge(1, 2)
        self.graph.add_edge(0, 3)

        self.assertEqual(self.graph.array[0].idx, 0)
        self.assertEqual(self.graph.array[1].idx, 1)
        self.assertEqual(self.graph.array[0].next.idx, 1)
        self.assertEqual(self.graph.array[0].next.next.idx, 3)
        self.assertEqual(self.graph.array[1].next.idx, 2)
        self.assertIsNone(self.graph.array[1].next.next)
        self.assertEqual(self.graph.array[0].next.val, 1)
        self.assertEqual(self.graph.array[1].next.val, 1)
        self.assertIsNone(self.graph.array[2])
        self.assertIsNone(self.graph.array[3])
        self.assertIsNone(self.graph.array[4])

        self.graph.add_edge(2, 3, 2)
        self.assertEqual(self.graph.array[2].next.idx, 3)
        self.assertEqual(self.graph.array[2].next.val, 2)
        self.assertIsNone(self.graph.array[3])

        self.graph.remove_edge(1, 2)
        self.assertIsNone(self.graph.array[1].next)
        self.assertEqual(self.graph.array[2].next.idx, 3)

        self.graph.remove_edge(2, 3)
        self.assertIsNone(self.graph.array[2].next)

        with self.assertRaises(IndexError):
            self.graph.remove_edge(0, 5)
        
        with self.assertRaises(ValueError):
            self.graph.remove_edge(2, 2)

        with self.assertRaises(ValueError):
            self.graph.remove_edge(2, 3)
        
        with self.assertRaises(ValueError):
            self.graph.remove_edge(3, 2)


if __name__ == '__main__':
    unittest.main()