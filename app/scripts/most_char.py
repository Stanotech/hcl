

def most_frequent_char(str):
    dic = {}
    for char in str:
        if char in dic:
            dic[char] += 1
        else:
            dic[char] = 1
    
    most = 0
    most_char = ""
    for key, value in dic.items():
        if value > most:
            most = value
            most_char = key

    return most_char


print(most_frequent_char("banana"))  # 'a' (bo 'a' występuje 3 razy, więcej niż inne znaki)
print(most_frequent_char("abcbcbc"))  # 'b' (bo 'b' i 'c' występują po 3 razy, ale 'b' pojawia się jako pierwszy)
print(most_frequent_char("xyz"))  # 'x' (każdy znak występuje raz, zwracamy pierwszy)