def most_char(s, k):
    actual = s[0]
    leng = 0
    longest = ("",0)
    for idx in range(len(s)):
        if s[idx] == actual:
            leng += 1
            if leng > len(longest[0]):
                longest = (s[idx-leng:idx+1], idx-leng)
        else:
            actual = s[idx]
            leng = 0

    if len(longest[0]) < k:
        longest = s[longest[1] : longest[1] + k]
    print(longest)

s = "aabbbccccdddeee"
k = 6

most_char(s, k)