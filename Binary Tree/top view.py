class newNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    
    def TopView(self, root):
    
        if root is None:
            return []

        ans = set()

        queue = [root]

        while queue:
            if queue[0]:
                ans.add(queue[0].val)

            if queue[-1]:
                ans.add(queue[-1].val)

            for i in range(len(queue)):
                node = queue.pop(0)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return ans

    
root = newNode(1)
root.left = newNode(2)
root.right = newNode(3)
root.left.right = newNode(4)
root.left.right.right = newNode(5)
root.left.right.right.right = newNode(6)
obj = Solution()
print(obj.TopView(root))