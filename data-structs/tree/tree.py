import wrappers
import sample_lists
from verify import verify
from node import TreeNode

class Tree:
    def __init__(self):
        self.root = None
        self.swaps = 0
        self.comparisons = 0
    
    def insert(self, val):
        if not self.root:
            self.root = TreeNode(val)
        else:
            pointer = self.root
            while True:
                self.comparisons += 1
                if val == pointer.val:
                    pointer.frequency += 1
                    break
                elif val < pointer.val:
                    if not pointer.left:
                        pointer.left = TreeNode(val)
                        break
                    pointer = pointer.left
                else:
                    if not pointer.right:
                        pointer.right = TreeNode(val)
                        break
                    pointer = pointer.right
    
    @wrappers.track_sort
    def sort(self, arr):
        for i in arr:
            self.insert(i)
        
        return self.swaps, self.comparisons, self.getSortedList()
    
    def getSortedList(self):
        return self.__getInOrder(self.root)
    
    def __getInOrder(self, node):
        if not node:
            return []
        return self.__getInOrder(node.left) + [node.val for _ in range(node.frequency)] + self.__getInOrder(node.right)
    
    def __repr__(self):
        return self.root.__repr__()
    
if __name__ == "__main__":
    tree = Tree()
    res = tree.sort(sample_lists.RANDOM_XTRA_LARGE)
    verify(res)
