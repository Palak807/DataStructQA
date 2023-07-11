class Solution(object):
    def partitionDisjoint(self, A):
       disjoint = 0
       curmax = leftmax = A[0]
       for i,num in enumerate(A):
           curmax = max(curmax, num)
           if num < leftmax:
               leftmax = curmax
               disjoint = i
       return disjoint + 1 
    
obj = Solution()
nums = [5,0,3,8,6]
print(obj.partitionDisjoint(nums))