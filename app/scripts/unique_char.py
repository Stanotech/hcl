def first_unique_char(str):
    dic = {}
    for idx, char in enumerate(str):
        if char in dic:
            dic[char].append(idx)
        else:
            dic[char] = [idx]

    for value in dic.values():
        if len(value) == 1: 
            return value[0]
    
    else:
        return -1



print(first_unique_char("loveleetcode"))  # 2  (bo 'v' jest pierwszym unikalnym znakiem)
print(first_unique_char("leetcode"))  # 0  (bo 'l' jest pierwszym niepowtarzającym się znakiem)
print(first_unique_char("aabb"))  # -1  (bo nie ma unikalnych znaków)
