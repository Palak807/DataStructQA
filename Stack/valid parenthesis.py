def is_balanced_parentheses(value):
    stack = []
    opening_brackets = ["(", "[", "{"]
    closing_brackets = [")", "]", "}"]

    for char in value:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if len(stack) == 0:
                return False
            top = stack.pop()
            if opening_brackets.index(top) != closing_brackets.index(char):
                return False

    return True