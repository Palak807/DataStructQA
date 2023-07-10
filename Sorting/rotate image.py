class Solution(object):
    def rotate(self, x):
        for i in range(len(x)):
            for j in range(i,len(x)):
                x[i][j],x[j][i]=x[j][i],x[i][j]
        for i in range(len(x)):
            x[i]=x[i][::-1]

obj = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
obj.rotate(matrix)
print(matrix)