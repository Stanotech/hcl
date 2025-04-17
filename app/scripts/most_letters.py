def top_letters(text, n):
    dic = {}
    text = text.lower().replace(" ", "")
    
    for char in text:
        if char in dic:
            dic[char] += 1
        else:
            dic[char] = 1

    sorted_dic = sorted(dic.items(), key = lambda item:item[1], reverse= True)
    return sorted_dic[:3]


text = "Ala ma kota, a kot ma Alę."
print(top_letters(text, 3))
# [('a', 5), ('m', 2), ('k', 2)]