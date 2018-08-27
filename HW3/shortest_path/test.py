import unittest
from shortest_path.shortest.path import trans,find_shortest_path


class Test_shortest_path(unittest.TestCase):
    def test_1(self):
        assert find_shortest_path("graph1.txt",1,4) == (3,['1,3,4'])

    def test_2(self):
        assert find_shortest_path("graph2.txt",1,4) == (-1,['1,2,3,4'])

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
