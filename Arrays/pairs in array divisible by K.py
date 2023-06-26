class Solution:
    def countKdivPairs(self, arr, n, k):
        d, count = {}, 0
        
        for i in arr:
            rem = i%k    
            if rem==0: count+=d.get(0, 0)
            else: count+=d.get(k-rem, 0)
            d[rem] = d.get(rem, 0)+1
        
        return count
    
obj = Solution()
A = {2, 2, 1, 7, 5, 3}
n = 6
K = 4

print(obj.countKdivPairs(A, n, K))