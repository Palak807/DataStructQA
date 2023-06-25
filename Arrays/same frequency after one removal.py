class Solution:
    def sameFreq(self, s):
        mapper = {}
        total = 0
        ans = "No"

        for i in range(len(s)):
            mapper[s[i]] = mapper.get(s[i], 0) + 1
        
        for count in mapper.values():
            total += count

        if total % len(mapper.keys()) == 0 :
            ans = "Yes"
        
        if (total - 1) % len(mapper.keys()) == 0 :
            ans = "Yes"
        
        return ans

obj = Solution()
print(obj.sameFreq("xxxxyyzz"))