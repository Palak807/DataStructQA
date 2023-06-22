class Solution:
    def isEularCircuitExist(self, N, graph):
        # code here
        count = 0
        for i in range(N):
            if len(graph[i]) % 2 == 1:
                count += 1
        if count == 0:
            return 1
        return 0 

obj = Solution()
N = 5
graph = [{0, 1, 0, 0, 1}, 
         {1, 0, 1, 1, 0}, 
         {0, 1, 0, 1, 0}, 
         {0, 1, 1, 0, 0}, 
         {1, 0, 0, 0, 0}]

print(obj.isEularCircuitExist(N, graph))