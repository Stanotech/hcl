# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.


def is_valid(string):
    stack = ""
    for i in range(len(string)):
        if string[i] in "{[(":
            stack += string[i]
        elif (
            string[i] == ")" and stack[-1] == "("
            or string[i] == "]" and stack[-1] == "["
            or string[i] == "}" and stack[-1] == "{"):
            
            stack = stack[:-1]

    if stack == "":
        return True
    else:
        return False


print(is_valid("()"))  # True
print(is_valid("()[]{}"))  # True
print(is_valid("(]"))  # False
print(is_valid("([)]"))  # False
print(is_valid("{[]}"))  # True
