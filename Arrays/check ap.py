class Solution:
    
    def checkIsAP(self, arr, n):
        arr.sort()

        d = arr[1] - arr[0]

        i = 1

        while i < n :
            if (arr[i] - arr[i - 1]) != d:
                return False
            i += 1
        
        return True




arr = [0, 12, 3, 8]
obj = Solution()
print(obj.checkIsAP(arr, 4))