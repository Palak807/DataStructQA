class Solution(object):
    def kSmallestPairs(self, nums1, k):

        mapper = {}
        mapper2 = {}
        nums1 = sorted(nums1)
        ans = []

        for i in nums1:
            mapper[i] = [k for k in nums1]

        for num, count in mapper.items():
            for i in count:
                if num <= i :
                    mapper2[num / i] = num, i
        
        mapper2 = sorted(mapper2.items())

        for i in range(len(mapper2)):
            ans.append(mapper2[i][1])

        
        return ans[k-1]


nums1 = [1, 2, 3, 5]

obj = Solution()
print(obj.kSmallestPairs(nums1, 3))