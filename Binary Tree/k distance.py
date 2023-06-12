# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, K):
        
        # dfs preorder traversal to map each node to its parent
        def get_parent(node = root, parent = None): #Hashmap
            if not node: return
            hashmap[node] = parent
            get_parent(node.left, node), get_parent(node.right, node)
        
        def search(node = target, distance = 0): #dfs
            if not node or node.val in visited: return
            visited.add(node.val)
            if distance == K: answer.append(node.val)
            for neighbour in (hashmap[node], node.left, node.right):
                search(neighbour, distance+1)
        
        hashmap, answer, visited = {}, [], set()
        get_parent(), search()
        return answer