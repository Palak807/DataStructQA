from collections import deque

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

def buildTree(s):
    if len(s) == 0 or s[0] == "N":
        return None

    ip = list(map(str, s.split()))
    root = Node(int(ip[0]))
    size = 0
    q = deque()
    q.append(root)
    size = size + 1
    i = 1

    while size > 0 and i < len(ip):
        currNode = q[0]
        q.popleft()
        size = size - 1

        currVal = ip[i]
        if currVal != "N":
            currNode.left = Node(int(currVal))
            q.append(currNode.left)
            size = size + 1

        i = i + 1
        if i >= len(ip):
            break
        currVal = ip[i]
        if currVal != "N":
            currNode.right = Node(int(currVal))
            q.append(currNode.right)
            size = size + 1

        i = i + 1

    return root

def printInorder(root):
    if root is None:
        return
    printInorder(root.left)
    print(root.data, end=" ")
    printInorder(root.right)


class Solution:
    # The given root is the root of the Binary Tree
    # Return the root of the generated BST
    def binaryTreeToBST(self, root):
        if root is None:
            return None

        root.left = self.binaryTreeToBST(root.left)
        root.right = self.binaryTreeToBST(root.right)

        if root.left is not None and root.left.data > root.data:
            root.data, root.left.data = root.left.data, root.data

        if root.right is not None and root.right.data < root.data:
            root.data, root.right.data = root.right.data, root.data

        return root


# Driver Code
if __name__ == "__main__":
    # Custom input
    t = 1
    s = "4 2 5 1 3 N 7"

    # Creating the binary tree
    root = buildTree(s)

    # Convert binary tree to BST
    solution = Solution()
    root = solution.binaryTreeToBST(root)

    # Print the in-order traversal of the modified BST
    printInorder(root)
