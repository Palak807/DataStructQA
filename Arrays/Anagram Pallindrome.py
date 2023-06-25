class Solution:

    def isPossible(self, S):
        mapper = {}
        count = 0

        for i in range(len(S)):
            mapper[S[i]] = mapper.get(S[i], 0) + 1
        
        for k in (mapper.values()):
            if k % 2 != 0:
                count += 1
                if count > 1:
                    return False
        
        return True

        
obj = Solution()
print(obj.isPossible("xxxxyyzz"))