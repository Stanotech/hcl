def most_char(s, k):    
    maxim = 0
    for idx in range(len(s)-k+1):
        str1 = s[idx:idx+k]
        dic = {}
        for char in str1:
            dic[char] = dic.get(char, 0) + 1
        
        dic_sorted = sorted(dic.items(), key = lambda item:item[1], reverse= True)
        if max(dic.values()) > maxim:
            longest = (str1, dic_sorted[0][0], dic_sorted[0][1])
            maxim = max(dic.values())

    print(longest)




s = "aabcbcbcaaa"
k = 5
most_char(s, k)