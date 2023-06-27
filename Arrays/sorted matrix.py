class Solution(object):
    def kthSmallest(self, matrix, k):
        ans = []

        for row in matrix:
            for column in row:
                ans.append(column)

        ans.sort()

        return (ans[k - 1])

obj = Solution()

matrix = [[1,5,9],
          [10,11,13],
          [12,13,15]]
k = 8
print(obj.kthSmallest(matrix, k))

        
        
