class Solution(object):
    def isValid(self, s):
        stack = []
        opening_brackets = ["(", "[", "{"]
        closing_brackets = [")", "]", "}"]

        for char in s:
            if char in opening_brackets:
                stack.append(char)
            elif char in closing_brackets:
                if len(stack) == 0:
                    return False
                top = stack.pop()
                if (top == "(" and char != ")") or (top == "[" and char != "]") or (top == "{" and char != "}"):
                    return False

        return len(stack) == 0
    
    def minAddToMakeValid(self, s):
        if self.isValid(s):
            return 0
        else:
            stack = []
            opening_brackets = ["(", "[", "{"]
            closing_brackets = [")", "]", "}"]

            missing_opening = 0

            for char in s:
                if char in opening_brackets:
                    stack.append(char)
                elif char in closing_brackets:
                    if len(stack) == 0:
                        missing_opening += 1
                    else:
                        stack.pop()

            return len(stack) + missing_opening 

value = "((()))(("
obj = Solution()
print(obj.minAddToMakeValid(value))
