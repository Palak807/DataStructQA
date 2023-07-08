class Solution(object):
    def majorityElement(self, nums):

        mapper = {}
        ans = 0

        for i in nums:
            mapper[i] = mapper.get(i, 0) + 1
            ans = max(mapper[i], ans)

        key_list = list(mapper.keys())
        val_list = list(mapper.values())
        
        return (key_list[val_list.index(ans)])

obj = Solution()
A = [2,2,1,1,1,2,2]
print(obj.majorityElement(A))