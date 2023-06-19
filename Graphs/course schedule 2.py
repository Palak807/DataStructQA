class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        class Graph:
            def __init__(self, numCourses):
                self.graph = {}
                self.V = numCourses

            def addEdge(self, u, v):
                if u not in self.graph:
                    self.graph[u] = []
                if v not in self.graph:
                    self.graph[v] = []
                self.graph[u].append(v)

            def topologicalSortUntil(self, v, visited, stack):
                visited[v] = True

                if v in self.graph:
                    for i in self.graph[v]:
                        if not visited[i]:
                            self.topologicalSortUntil(i, visited, stack)

                stack.append(v)

            def findOrder(self, numCourses, prerequisites):
                for pair in prerequisites:
                    self.addEdge(pair[1], pair[0])

                visited = [False] * self.V
                stack = []

                for i in range(self.V):
                    if not visited[i]:
                        self.topologicalSortUntil(i, visited, stack)

                return stack[::-1] if len(stack) == numCourses else []

        g = Graph(numCourses)
        return g.findOrder(numCourses, prerequisites)

obj = Solution()
numCourses = 2
prerequisites = [[1,0]]
print(obj.findOrder(numCourses, prerequisites))