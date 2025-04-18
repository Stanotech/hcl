def most_char(s, k):    
    longest = ""
    count = 0
    for idx in range(len(s)-k+1):
        dic = {}
        str1 = s[idx:idx+k]
        for char in str1:
            dic[char] = dic.get(char, 0) + 1
        
        maxim = max(dic.values())
        if maxim > count:
            count = maxim
            longest = str1

    print(longest)

s = "aabbbccccdddeee"
k = 6

most_char(s, k)