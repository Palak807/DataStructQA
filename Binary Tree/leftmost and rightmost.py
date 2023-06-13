# Definition for a binary tree node.
from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def levelOrder(self, root):
        if root is None:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_result = []
            level_size = len(queue)

            for _ in range(level_size):
                node = queue.popleft()
                level_result.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level_result)
        
        ans = set()

        for i in result:
            ans.add(i[0]), ans.add(i[-1])
        
        return ans
    
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)  
root.left.right = TreeNode(5)  
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)


obj = Solution()
print(obj.levelOrder(root))