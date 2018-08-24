class Tree(object):
    def __init__(self, root):
        """
        This is to initialize the root
        :param root : the root of the tree, which is in the format of Node
        """
        self.root = root
        
    def get_level(self,root):
        """
        This is to get the number of levels, or the depth, of the tree
        :param root : the root of the tree as a node, which is the upmost node of the tree
        :return : the number of levels of your tree
        """
        if root is None:
            return 0
        elif isinstance(root,Node) and root.left is None and root.right is None:
            return 1
        elif isinstance(root,Node):
            return max(self.get_depth(root.left),self.get_depth(root.right))+1
        else:
            return 1
    
    def insert(self,root,arr,row,col):
        """
        this can insert nodes to the desiered position of your tree
        :param root : the upmost node of your tree,in the format of Node
        :param arr : an array that contains every position and stucture of your tree
        :param row : an integer which specifies the the row position of the node
        :param col : an integer which specifies the column position of the node
        :return : the array with the node inserted
        """
        if isinstance(root, Node):
            arr[-row-1][col] = root.value
            if root.left:
                self.insert(root.left,arr,row-1,col-2**(row-1))
            if root.right:
                self.insert(root.right,arr,row-1,col+2**(row-1))
        else:
            arr[-row-1][col]=root
        return arr
    
    def printTree(self):
        """
        this can print the tree
        :return : your tree in the format of an array
        """
        depth = self.get_level(self.root)
        n = 2**depth-1
        arr = [['|'for i in range(n)]for j in range(depth)]
        arr = self.insert(self.root,arr,depth-1,2**(depth-1)-1)
        return arr  

class Node(object):

    def __init__(self, value, left, right):
        """
        this can specify how the node looks like
        :param value : the value of the node
        :param left : the value of the left branch of the node
        :param right : the value of the right branch of the node
        :return : the node with its value, left and right branches specified
        """
        self.value = value
        self.left = left
        self.right = right
        
if __name__ == '__main__':
    a = Node(1,Node(2,Node(3,None,None),Node(4,None,None)),Node(5,Node(6,None,None),Node(7,None,None)))
    b = Tree(a)
  
