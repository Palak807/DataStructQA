from collections import Counter
class Solution(object):
    def isLongPressedName(self, name, typed):
        # 1st approach
        map1 = Counter(name)
        map2 = Counter(typed)

        for key in map1:
            if map1[key] > map2.get(key, 0):
                return False
        return True
    
        # 2nd approach
        i = 0  
        j = 0  

        while j < len(typed):
            if i < len(name) and name[i] == typed[j]:
                i += 1
                j += 1
            elif j > 0 and typed[j] == typed[j - 1]:
                j += 1
            else:
                return False

        return i == len(name) and j == len(typed)


obj = Solution()
A="rick"
N = "kirc"
print(obj.isLongPressedName(N, A))