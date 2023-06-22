class Solution:
    def eulerPath(self, N, graph):
        # code here
        count = 0
        for i in range(N):
            if sum(graph[i]) % 2 == 0:
                count += 1
        if count == N-2:
            return 1
        return 0 

obj = Solution()
N = 5
graph = [{0, 1, 0, 0, 1}, 
         {1, 0, 1, 1, 0}, 
         {0, 1, 0, 1, 0}, 
         {0, 1, 1, 0, 0}, 
         {1, 0, 0, 0, 0}]

print(obj.eulerPath(N, graph))