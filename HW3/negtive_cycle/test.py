import unittest
from shortest_path.shortest.path import trans,find_shortest_path


class Test_negative_cycle(unittest.TestCase):
    def test_1(self):
        assert find_negative_cycles('graph1.txt') == None

    def test_2(self):
        assert find_negative_cycles('graph2.txt') == [1,3,2,1]
        
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
