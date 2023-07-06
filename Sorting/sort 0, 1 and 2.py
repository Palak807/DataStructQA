class Solution:
    def sort012(self,arr,n):
        
        mapper = {0: 0, 1: 0, 2: 0}

        for i in arr:
            mapper[i] += 1
    
        count_0 = mapper[0]
        count_1 = mapper[1]
    
        for i in range(count_0):
            arr[i] = 0

        for i in range(count_0, count_0 + count_1):
            arr[i] = 1

        for i in range(count_0 + count_1, n):
            arr[i] = 2

        return arr

arr = [0, 1, 0, 1, 1, 1, 2,2,2]
arr_size = len(arr)
print("Array after segregation")
obj = Solution()
print(obj.sort012(arr, arr_size))