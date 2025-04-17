def is_valid(str):
    dic = {"}":"{", "]":"[", ")":"("}
    stack = []

    for idx in range(len(str)):
        if str[idx] in dic.values():
            stack.append(str[idx])
        else:
            if dic[str[idx]] != stack[-1]:
                return False
            else:
                stack.pop(-1)
    
    if stack == []:
        return True


print(is_valid("()"))  # True
print(is_valid("()[]{}"))  # True
print(is_valid("(]"))  # False
print(is_valid("([)]"))  # False
print(is_valid("{[]}"))  # True