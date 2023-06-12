class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    
    def LeftView(self, root):
    
        if root is None:
            return []

        ans = []
        queue = [root]

        while queue:
            if queue[0]:
                ans.append(queue[0].val)

            for i in range(len(queue)):
                node = queue.pop(0)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return ans

    
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = None  
root.left.right = None  
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

obj = Solution()
print(obj.LeftView(root))