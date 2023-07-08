class Solution:
    
    def countOccurence(self,arr,n,k):
        mapper = {}
        ans = []

        for i in arr:
            mapper[i] = mapper.get(i, 0) + 1
        
        for key, value in mapper.items():
            if value > n / k  :
                ans.append(key)
        
        return len(ans)

obj = Solution()
N = 8
A = [3,1,2,2,1,2,3,3]
k = 4
print(obj.countOccurence(A, N, k))