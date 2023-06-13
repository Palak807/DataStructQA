# A Binary Tree Node
class Node:
	
	# A constructor to create new tree node
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None

def printSingles(root):

	if root is None:
		return

	if root.left is not None and root.right is not None:
		printSingles(root.left)
		printSingles(root.right)

	elif root.right is not None and root.left is None:
		print (root.right.key,end=" ")
		printSingles(root.right)

	elif root.left is not None and root.right is None:
		print (root.left.key,end=" ")
		printSingles(root.left)

# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(4)
root.right.left = Node(5)
root.right.left.left = Node(6)
printSingles(root)

