class Solution:
    def longestConsecutive(self, nums):
        nums = set(nums)
        best = 0
        for x in nums:
            if x - 1 not in nums:
                y = x + 1
                while y in nums:
                    y += 1
                best = max(best, y - x)
        return best

nums = [100,4,200,1,3,2]

obj = Solution()
print(obj.longestConsecutive(nums))