class Solution(object):
    def backspaceCompare(self, s, t):
        s1 = []
        s2 = []
        a1 = ""
        a2 = ""
        
        for i in range(len(s)):
            if s[i] == "#":
                if len(s1) > 0:
                    s1.pop()
            else:
                s1.append(s[i])
        
        for i in range(len(t)):
            if t[i] == "#":
                s2.pop()
            else:
                s2.append(t[i])

        for j in range(len(s1)):
            a1 += s1[j]

        for k in range(len(s2)):
            a2 += s2[k]

        if a1 == a2 :
            return True
        else:
            return False

s = "abb#"
t = "a#ab"
obj = Solution()
print(obj.backspaceCompare(s,t))