def almost_anagrams(str1, str2):
    def dictionerize(string):
        dic= {}
        for idx, char in enumerate(string):
            if char in dic:
                dic[char] += 1
            else:
                dic[char] = 1
        return dic
    
    str1_dic = dictionerize(str1)
    str2_dic = dictionerize(str2)
    print(str1_dic)
    print(str2_dic)
    for key, value in str1_dic.items():
        if key in str2_dic:
            if str2_dic[key] == value:
                str2_dic.pop(key)
            else:
                str2_dic[key] -= str1_dic[key]
        
    list_dic = (list(str2_dic.values()))
    if list_dic[0]==1 and len(list_dic)==1:
        print(True)
    else:
        print(False)
    



almost_anagrams("bake", "cake")  # True (zmiana 'b' na 'c')
almost_anagrams("listen", "lispen")  # True (zmiana 't' na 'p')
almost_anagrams("hello", "heppo")  # False (trzeba zmienić dwa znaki: 'l' na 'p' i 'l' na 'o')
almost_anagrams("apple", "appla")  # True (zamiana 'e' na 'a')
almost_anagrams("test", "tent")  # True (zmiana 's' na 'n')