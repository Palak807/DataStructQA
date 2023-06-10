# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        if root is None:
            return root
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # Case 1: No child or only one child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            
            # Case 2: Two children
            min_node = self.findMin(root.right)
            root.val = min_node.val
            root.right = self.deleteNode(root.right, min_node.val)
        
        return root
    
    def findMin(self, node):
        while node.left:
            node = node.left
        return node
