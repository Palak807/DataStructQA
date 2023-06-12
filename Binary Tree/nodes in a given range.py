# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    def getCount(self, root, l, h):

        def preOrder(node):
            if node is None:
                return []
            result = [node.val]
            result += preOrder(node.left)
            result += preOrder(node.right)
            return result

        result = preOrder(root)
        ans = []
        for i in result:
            if l <= i <= h:
                ans.append(i)
        return ans


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = None  
root.left.right = None  
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

obj = Solution()

print(obj.getCount(root, 2, 5))
