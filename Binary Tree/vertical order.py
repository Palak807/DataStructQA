class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def verticalTraversal(self, root):
        mapper = {}

        def dfs(x, y, node):
            if node is None:
                return
            if (x, y) not in mapper:
                mapper[(x, y)] = []
            dfs(x - 1, y + 1, node.left)
            dfs(x + 1, y + 1, node.right)
            mapper[(x, y)].append(node.val)

        dfs(0, 0, root)

        output = []
        old = float('-inf')
        for k, v in sorted(mapper.items()):
            if k[0] != old:
                output.append([])

            output[-1].extend(sorted(v))
            old = k[0]

        return output



    
    
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)  
root.left.right = TreeNode(5)  
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

obj = Solution()
print(obj.verticalTraversal(root))
