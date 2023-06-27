class Solution(object):
    def canPair(self, nums1, k):
        nums1 = sorted(nums1)
        ans = []

        for i in nums1:
            for j in nums1:
                if i <= j:
                    pair_sum = i + j
                    if pair_sum % k == 0:
                        ans.append((i, j))

        if len(ans) == 0:
            return False
        else:
            return True

nums1 = [9, 7, 5, 3]
obj = Solution()
print(obj.canPair(nums1, 6))
