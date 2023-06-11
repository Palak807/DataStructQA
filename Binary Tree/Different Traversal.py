# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    def preOrder(self, root):

        if root is None :
            return 

        result = []

        temp = root 
        result.append(temp.val)
        if temp.left is not None:
            result += self.preOrder(temp.left)
        if temp.right is not None:
            result += self.preOrder(temp.right)
        
        return result
     
    def inorderTraversal(self, root):

        if root is None :
            return 

        result = []

        temp = root 
        if temp.left is not None:
            result += self.inorderTraversal(temp.left)
        result.append(temp.val)
        if temp.right is not None:
            result += self.inorderTraversal(temp.right)
        
        return result

    def postorderTraversal(self, root):

        if root is None :
            return 

        result = []

        temp = root 
        if temp.left is not None:
            result += self.postorderTraversal(temp.left)
        if temp.right is not None:
            result += self.postorderTraversal(temp.right)
        result.append(temp.val)
        
        return result

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = None  
root.left.right = None  
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

obj = Solution()
print(obj.preOrder(root))
print(obj.inorderTraversal(root))
print(obj.postorderTraversal(root))