class Solution:
    def findMotherVertex(self, V, adj):
        def dfs(adj, s, visited):
            visited[s] = True
            for u in adj[s]:
                if visited[u] == False:
                    dfs(adj, u, visited)

        visited = [False] * V  
        res = -1
        for i in range(V):
            if visited[i] == False:
                dfs(adj, i, visited)
                res = i

        visited = [False] * V 
        dfs(adj, res, visited)

        if all(visited):
            return res 

        return -1


# Driver code
if __name__ == '__main__':
    T = 1  
    for _ in range(T):
        V, E = 4, 3  
        adj = [[1, 2], [2], [], []]  # Adjusted adjacency list
        obj = Solution()
        ans = obj.findMotherVertex(V, adj)
        print(ans)
