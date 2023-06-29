class Solution:
    def countElements(self,N,A):
        
        result = max(A) - min(A) - 1
        
        existing = set(A)
        present = len(existing) - 2

        result -= present

        return result
        


obj = Solution()
A=[205,173,102,324,957]
N = 5
print(obj.countElements(N, A))