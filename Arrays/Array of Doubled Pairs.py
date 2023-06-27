class Solution(object):
    def canReorderDoubled(self, arr):
        counts = {}
        
        for num in arr:
            counts[num] = counts.get(num, 0) + 1

        n = [i for i in arr if i < 0]
        p = [i for i in arr if i >= 0]

        arr = sorted(n, reverse= True) + sorted(p)

        for k in arr:
            if counts.get(k, 0) == 0:
                continue

            if counts.get(2 *k, 0) == 0:
                return False
            
            counts[k] -= 1
            counts[2 * k] -= 1
        
        return True
        
        

obj = Solution()
arr = [3,6,3,6]

print(obj.canReorderDoubled(arr))