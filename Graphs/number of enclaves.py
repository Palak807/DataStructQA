from collections import deque

class Solution:
    def enclaves(self, grid):
        ROW, COLS = len(grid), len(grid[0])

        for r in range(ROW):
            for c in range(COLS):
                if (r == 0 or r == ROW - 1 or c == 0 or c == COLS - 1) and grid[r][c] == 1:
                    self.dfs(grid, r, c)

        count = 0
        for r in range(ROW):
            for c in range(COLS):
                if grid[r][c] == 1:
                    count += 1

        return count

    def dfs(self, grid, r, c):
        ROW, COLS = len(grid), len(grid[0])

        if r < 0 or r >= ROW or c < 0 or c >= COLS or grid[r][c] != 1:
            return

        grid[r][c] = 0  

        self.dfs(grid, r + 1, c)  
        self.dfs(grid, r - 1, c)  
        self.dfs(grid, r, c + 1)  
        self.dfs(grid, r, c - 1)  





solution = Solution()
grid = [
    [0, 0, 0, 0],
    [1, 0, 1, 0],
    [0, 1, 1, 0],
    [0, 0, 0, 0]
]
result = solution.enclaves(grid)
print(result)
