class Solution:
    def longestOnes(self, A, K):
      left = right = 0
      
      for right in range(len(A)):

        if A[right] == 0:
          K -= 1

        if K < 0:
          if A[left] == 0:
            K += 1
          left += 1
      
      return right - left + 1
    

obj = Solution()
A = [1,1,1,0,0,0,1,1,1,1,0]
K = 2
print(obj.longestOnes(A, K))