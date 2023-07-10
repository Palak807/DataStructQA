class Solution(object):
    def numSubarrayBoundedMax(self, nums, left, right):
        ans, low, mid = 0, 0, 0
        for num in nums:
            if num > right: mid = 0
            else:
                mid += 1
                ans += mid
            if num >= left: low = 0
            else:
                low += 1
                ans -= low
        return ans

nums = [2,1,4,3]
left = 2
right = 3
obj = Solution()
print(obj.numSubarrayBoundedMax(nums,left,right))