from collections import deque


class Solution:
    def orangesRotting(self, grid):

        q = deque()
        time, fresh = 0, 0

        ROW, COLS = len(grid), len(grid[0])

        for r in range(ROW):
            for c in range(COLS):
                if grid[r][c]== 1:
                    fresh += 1
                if grid[r][c]== 2:
                    q.append([r,c])

        neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while q and fresh > 0:

            for i in range(len(q)):
                r, c = q.popleft()

                for dr, dc in neighbors:
                    row, col = dr + r, dc +c
                    if (row < 0 or row == len(grid) or
                        col < 0 or col == len(grid[0]) or
                        grid[row][col] != 1):
                        continue
                    grid[row][col] = 2
                    q.append((r + dr, c + dc))
                    fresh -= 1
            time += 1
        
        return time if fresh == 0 else -1
