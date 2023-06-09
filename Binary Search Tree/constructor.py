class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
            return True
        temp = self.root
        while(True): 
            if new_node.value == temp.value :
                return False
            elif new_node.value < temp.value :
                if temp.left == None:
                    temp.left = new_node
                    return True
                temp = temp.left
            elif new_node.value > temp.value :
                if temp.right == None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def search(self, value):
        temp = self.root
        while (temp):
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            elif value == temp.value:
                return True
        return False
            

    def print_tree(self):
        self._print_helper(self.root)

    def _print_helper(self, node):
        if node is None:
            return
        self._print_helper(node.left)
        print(node.value)
        self._print_helper(node.right)

my_tree = BinarySearchTree()
my_tree.insert(9)
my_tree.insert(5)
my_tree.insert(15)
my_tree.insert(24)
print(my_tree.search(50))
my_tree.print_tree()