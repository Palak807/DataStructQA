class Solution(object):
    def scoreOfParentheses(self, s):
        stack = []
        opening_brackets = ["(", "[", "{"]
        closing_brackets = [")", "]", "}"]
        score = 0

        for char in s:
            if char in opening_brackets:
                stack.append(char)
            elif char in closing_brackets:
                if len(stack) == 0:
                    continue
                top = stack.pop()
                score += 1
                if (top == "(" and char != ")") or (top == "[" and char != "]") or (top == "{" and char != "}"):
                    continue

        return score
    
    # 2nd approach :

    # class Solution(object):
    # def scoreOfParentheses(self, s):
    #     stack = []
    #     score = 0

    #     for char in s:
    #         if char == '(':
    #             stack.append(score)
    #             score = 0  
    #         elif char == ')':
    #             if len(stack) == 0:
    #                 continue
    #             score_inside = stack.pop()  
    #             score = score_inside + max(score * 2, 1)  

    #     return score


value = "((()))(())"
obj = Solution()
print(obj.scoreOfParentheses(value))