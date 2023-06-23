class Solution(object):
    def canReorderDoubled(self, arr):
        counts = {}
        
        for num in arr:
            counts[num] = counts.get(num, 0) + 1
        
        arr.sort()
        
        for num in arr:
            if counts[num] == 0: 
                continue
            
            if num < 0:  
                if num % 2 != 0 or num // 2 not in counts or counts[num // 2] == 0:
                    return False
                counts[num] -= 1
                counts[num // 2] -= 1
            else:  
                if num * 2 not in counts or counts[num * 2] == 0:
                    return False
                counts[num] -= 1
                counts[num * 2] -= 1
        
        return True
