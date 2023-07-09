class Solution(object):
    def firstMissingPositive(self, nums):

        nums.sort()

        b = 1

        for i in range(len(nums)):
            if nums[i] == b:
                b += 1
        
        return b 

obj = Solution()
arr = [1,2,4,5,7]
print(obj.firstMissingPositive(arr))