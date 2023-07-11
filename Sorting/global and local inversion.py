class Solution(object):
    def isIdealPermutation(self, nums):

        LI = GI = 0

        for i in range(len(nums)- 1):
            if nums[i] > nums[i + 1]:
                LI += 1
            
            for j in range(len(nums)):
                if j > i and nums[i] > nums[j]:
                    GI += 1
        
        return True if LI == GI else False

obj = Solution()
arr = [1,0,2]
print(obj.isIdealPermutation(arr))