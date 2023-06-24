class Solution:
    def longestSubstrDistinctChars(self, S):
        max_length = 0
        start = 0
        char_map = {}
        longest_substr = ""

        for end in range(len(S)):
            if S[end] in char_map:
                start = max(start, char_map[S[end]] + 1)
            char_map[S[end]] = end
            if end - start + 1 > max_length:
                max_length = end - start + 1
                longest_substr = S[start:end+1]

        return max_length, longest_substr

obj = Solution()
S = "geeksforgeeks"
length, substr = obj.longestSubstrDistinctChars(S)
print("Longest substring length:", length)
print("Longest substring:", substr)
