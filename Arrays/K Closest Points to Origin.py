import math 

class Solution(object):
    def kClosest(self, points, k):
        result = {}
        ans = []

        for i in range(len(points)):
            x = points[i][0]
            y = points[i][1]
            distance = math.sqrt(math.pow((0-x),2) + math.pow((0-y),2))

            result[tuple(points[i])] = distance
        
        for i in range(k):

            result = sorted(result)
            ans.append(result[i])
 
        return ans
        

obj = Solution()
points = [[3,3],[5,-1],[-2,4]]
k = 2
print(obj.kClosest(points, k))