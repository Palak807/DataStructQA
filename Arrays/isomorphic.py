class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False

        m1 = {}
        m2 = {}

        for i in range(len(s)):
            m1[s[i]] = m1.get(s[i], 0) + 1
            m2[t[i]] = m2.get(t[i], 0) + 1

        return list(m1.values()) == list(m2.values())

obj = Solution()
print(obj.isIsomorphic("paper", "title"))  # Output: True
