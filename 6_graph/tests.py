import adjacency_matrix_graph as mg
import adjacency_list_graph as lg
import unittest


class MatrixUndirectedGraphTest(unittest.TestCase):
    def setUp(self):
        self.graph = mg.UndirectedGraph()
    
    def test_add_edge(self):
        pass

    def test_remove_edge(self):
        pass


class MatrixDirectedGraphTest(unittest.TestCase):
    def setUp(self):
        self.graph = mg.DirectedGraph()

    def test_add_edge(self):
        pass

    def test_remove_edge(self):
        pass


class LinkedListUndirectedGraphTest(unittest.TestCase):
    def setUp(self):
        self.graph = lg.UndirectedGraph()

    def test_add_edge(self):
        pass

    def test_remove_edge(self):
        pass


class LinkedListDirectedGraphTest(unittest.TestCase):
    def setUp(self):
        self.graph = lg.DirectedGraph()

    def test_add_edge(self):
        pass

    def test_remove_edge(self):
        pass
