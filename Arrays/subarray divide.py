class Solution(object):
    def subCount(self,arr, n, k):
        # Your code goes here
        count = 0
        sums = 0
        ans = 0
        d = {0: 1}
        
        for i in range(n):
            sums += arr[i]
            ans = sums % k
            count += d.get(ans,0)
            d[ans] = d.get(ans,0) + 1
        
        return(count)
    
obj = Solution()
nums = [3,4,7]
k = 7

print(obj.subarrayDivide(nums, k))