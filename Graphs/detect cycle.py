class Solution(object):
    def isCycle(self, graph):
        def dfs(node, adjList, visited, parent):
            visited[node] = True
            for neighbor in adjList[node]:
                if not visited[neighbor]:
                    if dfs(neighbor, adjList, visited, node):
                        return True
                elif parent != neighbor:
                    return True
            return False

        visited = [False] * len(graph)
        for i in range(len(graph)):
            if not visited[i]:
                if dfs(i, graph, visited, -1):
                    return True
        return False


graph = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]
obj = Solution()
print(obj.isCycle(graph))
