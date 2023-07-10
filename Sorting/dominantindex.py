import heapq


class Solution(object):
    def dominantIndex(self, nums):
        
        largest = heapq.nlargest(1,nums)
        ans = (nums.index(largest[0]))
        nums.remove(largest[0])

        for i in nums:
            if largest[0] < 2 * i:
                return -1
        return ans


obj = Solution()
arr = [0,2,6]
print(obj.dominantIndex(arr))