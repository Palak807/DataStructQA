class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def buildTree(self, inorder, postorder):

        if not postorder or not inorder:
            return None

        root = TreeNode(postorder[-1])
        mid = inorder.index(postorder[-1]) #Finding the index of the root in inorder list 
        

        root.left = self.buildTree(inorder[0:mid], postorder[0:mid]) # 1 to index(from inorder) + 1  is left subtree in postorder
        root.right = self.buildTree(inorder[mid + 1:], postorder[mid: -1])

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
postorder = [9, 15, 7, 20, 3]
inorder = [9, 3, 15, 20, 7]

root = object.buildTree(inorder, postorder)
object.printTree(root)
