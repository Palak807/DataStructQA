class Solution(object):
    def isBipartite(self, graph):
        mapper = {}
        for i in range(len(graph)):
            mapper[i] = graph[i]

        def dfs(node, adjList, visit, colors):
            visit.add(node)
            for neighbor in adjList[node]:
                if neighbor not in visit:
                    colors[neighbor] = 1 - colors[node]  
                    if not dfs(neighbor, adjList, visit, colors):
                        return False
                elif colors[neighbor] == colors[node]:
                    return False
            return True

        visit = set()
        colors = {}  
        for node in mapper:
            if node not in visit:
                colors[node] = 0 
                if not dfs(node, mapper, visit, colors):
                    return False
        return True
        
            


graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
obj = Solution()
obj.isBipartite(graph)