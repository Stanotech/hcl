def min_window_substring(str, letters):
    dic = {}
    short_len = len(str)
    shortest = ""
    for idx, char in enumerate(str):

        if char in letters:
            dic[char] = idx
        sort = sorted(dic.values())

        if len(dic.keys()) == len(letters):
            if short_len > sort[-1] - sort[0]:
                short_len = sort[-1] - sort[0]
                shortest = str[sort[0]:sort[-1]+1]
    
    print(shortest)


min_window_substring("ADOBECODEBANC", "ABC")  # "BANC"
min_window_substring("a", "a")  # "a"
min_window_substring("a", "aa")  # "" (brakuje jednego 'a')
min_window_substring("abcd", "bd")  # "bd"