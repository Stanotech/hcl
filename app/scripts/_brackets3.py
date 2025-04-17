def is_valid(str):
    dic = { "}" : "{", "]" : "[", ")": "("}
    stack = []
    for char in str:
        if char not in dic :
            stack.append(char)
        else:
            if dic[char] == stack[-1]:
                stack.pop()
            else:
                return False
    
    if stack == []:
        return True



print(is_valid("()"))  # True
print(is_valid("()[]{}"))  # True
print(is_valid("(]"))  # False
print(is_valid("([)]"))  # False
print(is_valid("{[]}"))  # True