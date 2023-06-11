class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def buildTree(self, levelorder, inorder):
        if not levelorder or not inorder:
            return None

        root_val = levelorder.pop(0)  # Get the root value from levelorder list
        root = TreeNode(root_val)
        mid = inorder.index(root_val)

        # Split the inorder list based on the root index
        inorder_left = inorder[:mid]
        inorder_right = inorder[mid + 1:]

        # Find the elements in levelorder list that belong to the left and right subtrees
        levelorder_left = [val for val in levelorder if val in inorder_left]
        levelorder_right = [val for val in levelorder if val in inorder_right]

        root.left = self.buildTree(levelorder_left, inorder_left)
        root.right = self.buildTree(levelorder_right, inorder_right)

        return root

    def printTree(self, root):
        self._printTree(root, 0)

    def _printTree(self, node, level):
        if node is None:
            return

        self._printTree(node.right, level + 1)
        print('    ' * level + str(node.val))
        self._printTree(node.left, level + 1)


object = Solution()
levelorder = [20, 8, 22, 4, 12, 10, 14]
inorder = [4, 8, 10, 12, 14, 20, 22]

root = object.buildTree(levelorder, inorder)
object.printTree(root)
