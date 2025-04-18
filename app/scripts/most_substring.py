def most_frequent_unique_triplet(s):
    unique_substrings = []
    for idx in range(len(s)-2):
        str1 = s[idx:idx+3]
        dic= {}
        for char in str1:
            dic[char] = dic.get(char, 0) + 1
        if list(dic.values()) == [1,1,1]:
            unique_substrings.append(str1)
    
    max_count = 0
    max_substr =""
    for substr in set(unique_substrings):
        if unique_substrings.count(substr) > max_count:
            max_count = unique_substrings.count(substr)
            max_substr = substr

    return max_substr



s = "abcbacabcabc"

najczestszy_3 = most_frequent_unique_triplet(s)
print(najczestszy_3)  # powinno wypisać: "abc"

