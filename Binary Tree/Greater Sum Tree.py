# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def bstToGst(self, root):

        self.sum = 0
        
        def dfs(node):
            if node is None:
                return
            
            dfs(node.right)
            
            node.val += self.sum
            
            self.sum = node.val
            
            dfs(node.left)
        
        dfs(root)
        
        return root


root = TreeNode(4)
root.left = TreeNode(1)
root.right = TreeNode(6)
root.left.left = TreeNode(0)
root.left.right = TreeNode(2)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)
root.left.left.left = None
root.left.left.right = None
root.left.right.left = TreeNode(3)
root.left.right.right = None
root.right.left.left = None
root.right.left.right = None
root.right.right.left = None
root.right.right.right = TreeNode(8)

obj = Solution()

print(obj.bstToGst(root))