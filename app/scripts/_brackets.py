# HCl. Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.


def is_valid(string):
    bracket_map = {')': '(', '}': '{', ']': '['}
    stack = []
    for i in range(len(string)):
        if string[i] in "{[(":
            stack.append(string[i])
        elif stack[-1] == bracket_map[string[i]]:
            stack.pop()

    if stack == []:
        return True
    else:
        return False


print(is_valid("()"))  # True
print(is_valid("()[]{}"))  # True
print(is_valid("(]"))  # False
print(is_valid("([)]"))  # False
print(is_valid("{[]}"))  # True
