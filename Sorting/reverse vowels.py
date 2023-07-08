class Solution(object):
    def reverseVowels(self, s):
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        ans = list(s)
        i, j = 0, len(s) - 1

        while i < j:
            if ans[i] in vowels and ans[j] in vowels:
                ans[i], ans[j] = ans[j], ans[i]
                i += 1
                j -= 1
            elif ans[i] in vowels:
                j -= 1
            elif ans[j] in vowels:
                i += 1
            else:
                i += 1
                j -= 1

        return ''.join(ans)


obj = Solution()
print(obj.reverseVowels("hello"))  # Output: "holle"
print(obj.reverseVowels("leetcode"))  # Output: "leotcede"
