class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1:mid + 1], inorder[0:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

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
preorder = [6, 2, 0, 4, 3, 5, 8, 7, 9]
inorder = [0, 2, 3, 4, 5, 6, 7, 8, 9]

root = object.buildTree(preorder, inorder)
object.printTree(root)
