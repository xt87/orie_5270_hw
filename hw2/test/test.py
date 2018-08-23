import unittest
from tree.tree import Tree,Node

class TestPrintTree(unittest.TestCase):
    def test_1(self):
        self.test = Node(3,None,None)
        self.answer = [[3]]
        assert Tree(self.test).printTree()== self.answer
        
    def test_2(self):
        self.test = Node(1,Node(2,Node(3,None,None),Node(4,None,None)),Node(5,Node(6,None,None),Node(7,None,None)))
        self.answer = [['|','|','|',1,'|','|','|'],
                       ['|',2,'|','|','|',5,'|'],
                       [3,'|',4,'|',6,'|',7]]
        assert Tree(self.test).printTree()== self.answer

    def test_3(self):
        self.test = Node(1,Node(1,Node(1,Node(1,None,None),None),None),None)
        self.answer = [['|','|','|','|','|','|','|',1,'|','|','|','|','|','|','|'],
                       ['|','|','|',1,'|','|','|','|','|','|','|','|','|','|','|'],
                       ['|',1,'|','|','|','|','|','|','|','|','|','|','|','|','|'],
                       [1,'|','|','|','|','|','|','|','|','|','|','|','|','|','|'],]
        assert Tree(self.test).printTree()== self.answer
        
    def test_4(self):
        self.test = Node(1,Node(1,None,1),Node(1,Node(1,None,1),None))
        self.answer = [['|','|','|','|','|','|','|',1,'|','|','|','|','|','|','|'],
                       ['|','|','|',1,'|','|','|','|','|','|','|',1,'|','|','|'],
                       ['|','|','|','|','|',1,'|','|','|',1,'|','|','|','|','|'],
                       ['|','|','|','|','|','|','|','|','|','|',1,'|','|','|','|'],]
        assert Tree(self.test).printTree()== self.answer
        
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
