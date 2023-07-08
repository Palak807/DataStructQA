class Solution(object):
    def majorityElement(self, nums):
        
        mapper = {}
        ans = []

        for i in nums:
            mapper[i] = mapper.get(i, 0) + 1
        
        for key, value in mapper.items():
            if value > len(nums)/3 :
                ans.append(key)
        
        return ans

obj = Solution()
A = [2,2,1,1,1,2,2]
print(obj.majorityElement(A))