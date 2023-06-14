class Solution(object):
    def islandPerimeter(self, grid):
        perimeter = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    perimeter += 4
                    if i != 0 and grid[i-1][j] == 1:
                        perimeter -= 2
                    if j != 0 and grid[i][j-1] == 1:
                        perimeter -= 2 
            
        return perimeter
    
obj = Solution()

grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]

print(obj.islandPerimeter(grid))