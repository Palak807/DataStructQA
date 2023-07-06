class Solution():
    def hasArrayTwoCandidates(self, arr, n, x):
        mapper = {}

        for num in arr:
            complement = x - num
            if complement in mapper:
                return True
            mapper[num] = True

        return False



nums = [3, 1, 2, 4, 3]
obj = Solution()
print(obj.hasArrayTwoCandidates(nums, 5, 9))
