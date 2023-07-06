class Solution(object):
    def sortArrayByParity(self, nums):
        left, right = 0, len(nums) - 1

        while left < right:
            if nums[left] % 2 != 0 and nums[right] % 2 == 0:
                nums[left], nums[right] = nums[right], nums[left]
            elif nums[left] % 2 == 0:
                left += 1
            elif nums[right] % 2 != 0:
                right -= 1
        
        return nums

    
nums = [3,1,2,4]
obj = Solution()
print(obj.sortArrayByParity(nums))