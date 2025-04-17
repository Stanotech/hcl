def first_unique_char(str):
    dic = {}
    for char in str:
        dic[char] = dic.get(char, 0) + 1

    for key, value in dic.items():
        if value == 1:
            return key
    return ""
        





print(first_unique_char("aabbccdeff"))   # ➞ "d"
print(first_unique_char("aabb"))         # ➞ ""
print(first_unique_char("racecars"))     # ➞ "e"
print(first_unique_char("redivider"))    # ➞ "v"