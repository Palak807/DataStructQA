class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def findTilt(self, root):
        self.total_tilt = 0

        def calculateTilt(node):
            if node is None:
                return 0

            left_sum = calculateTilt(node.left)
            right_sum = calculateTilt(node.right)

            tilt = abs(left_sum - right_sum)
            self.total_tilt += tilt

            return node.val + left_sum + right_sum

        calculateTilt(root)
        return self.total_tilt


    
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)  
root.left.right = TreeNode(5)  
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

obj = Solution()
print(obj.findTilt(root))
