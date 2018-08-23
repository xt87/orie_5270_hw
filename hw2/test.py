import unittest

class TestPrintTree(unittest.TestCase):
    def test1(self):
        self.test = Node(3,None,None)
        self.answer = [[3]]
        assert Tree(self.test).printTree()== self.answer
        
    def test2(self):
        self.test = Node(1,Node(2,Node(3,None,None),Node(4,None,None)),Node(5,Node(6,None,None),Node(7,None,None)))
        self.answer = [['|','|','|',1,'|','|','|'],
                       ['|',2,'|','|','|',5,'|'],
                       [3,'|',4,'|',6,'|',7]]
        self.assertEqual(Tree(self.test).printTree(),self.answer)

   
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
