# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    def kthSmallest(self, root, k):

        def preOrder(root):

            if root is None :
                return 

            result = []

            temp = root 
            result.append(temp.val)
            if temp.left is not None:
                result += preOrder(temp.left)
            if temp.right is not None:
                result += preOrder(temp.right)
            
            return result
        
        ans = preOrder(root)
        ans.sort()
        if ans[k - 1] is not None :
            return ans[k - 1]
        else :
            return None
     

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)  
root.left.right = TreeNode(5)  
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)


obj = Solution()
print(obj.kthSmallest(root, 5))
