# class to represent Nodes in the Tree
# it is designed this way because I like accessing instance vars with functions
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.frequency = 1
    
    def isLeaf(self):
        return self.left == self.right == None
    
    def __repr__(self, level=0):
        ret = "-" * level + repr(self.value) + "\n"
        ret += self.left.__repr__(level + 1)
        ret += self.right.__repr__(level + 1)
        return ret