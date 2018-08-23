class Tree(object):
    def __init__(self, root):
        self.root = root

    def get_value_root(self):
        if self.root is not None:
            return self.root.value
        else:
            return None
        
    def get_depth(self,root):
        if root is None:
            return 0
        elif isinstance(root,Node) and root.left is None and root.right is None:
            return 1
        elif isinstance(root,Node):
            return max(self.get_depth(root.left),self.get_depth(root.right))+1
        else:
            return 1
    
    def insert(self,root,arr,row,col):
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
        depth = self.get_depth(self.root)
        n = 2**depth-1
        arr = [['|'for i in range(n)]for j in range(depth)]
        arr = self.insert(self.root,arr,depth-1,2**(depth-1)-1)
        return arr  
