class Solution(object):
    def subarraySum(self, nums, k):

        count = 0
        sums = 0
        d = dict()
        d[0] = 1
        
        for i in range(len(nums)):
            sums += nums[i]
            count += d.get(sums-k,0)
            d[sums] = d.get(sums,0) + 1
        
        return(count)
    
obj = Solution()
nums = [3,4,7]
k = 7

print(obj.subarraySum(nums, k))