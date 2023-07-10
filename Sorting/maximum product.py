import heapq


class Solution(object):
    def maximumProduct(self, nums):
       
       pos=heapq.nlargest(3,nums)
       print(pos)
       neg=heapq.nsmallest(2,nums)

       p1 = neg[0]*neg[1]*pos[0]

       p2 = pos[0]*pos[1]*pos[2]

       return max(p1,p2)
        

obj = Solution()
arr = [0,2,3]
print(obj.maximumProduct(arr))