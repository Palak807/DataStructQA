from collections import deque

class StoneRemovalSolution:
    def removeStones(self, stones):
        ROW, COL = {}, {}  
        count = 0  

        for stone in stones:
            x, y = stone
            ROW[x] = ROW.get(x, []) + [stone]
            COL[y] = COL.get(y, []) + [stone]

        visited = set()  

        for stone in stones:
            if tuple(stone) not in visited:
                count += self.bfs(stone, ROW, COL, visited)

        return count

    def bfs(self, stone, ROW, COL, visited):
        queue = deque([stone])
        visited.add(tuple(stone))
        count = 0

        while queue:
            curr_stone = queue.popleft()
            x, y = curr_stone

            for neighbor in ROW[x]:
                if tuple(neighbor) not in visited:
                    queue.append(neighbor)
                    visited.add(tuple(neighbor))
                    count += 1

            for neighbor in COL[y]:
                if tuple(neighbor) not in visited:
                    queue.append(neighbor)
                    visited.add(tuple(neighbor))
                    count += 1

        return count


solution = StoneRemovalSolution()
stones = [[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]
result = solution.removeStones(stones)
print(result)
