class Solution(object):
    def decodeString(self, s):
        s1 = []
        i = 0
        while i < len(s):
            if s[i].isdigit():
                count = 0
                while s[i].isdigit():
                    count = count * 10 + int(s[i])
                    i += 1
                s1.append(str(count))
            elif s[i] == '[':
                s1.append('[')
                i += 1
            elif s[i] == ']':
                decoded_string = ''
                while s1[-1] != '[':
                    decoded_string = s1.pop() + decoded_string
                s1.pop()  # Pop '['
                count = int(s1.pop())
                s1.append(count * decoded_string)
                i += 1
            else:
                s1.append(s[i])
                i += 1

        return ''.join(s1)

value = "100[leetcode]"
obj = Solution()
print(obj.decodeString(value))
