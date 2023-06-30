class Solution(object):
    def rotate(self, nums, k):

        for i in range(k):
            nums.insert(0, nums[len(nums)-1])
            nums.pop()

        return nums
        


obj = Solution()
arr = [1,2,3,4,5,6,7]
k = 3
print(obj.rotate(arr, k))