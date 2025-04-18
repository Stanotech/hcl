def erase(s):
    erase_list = []
    for idx in range(len(s)-1):
        if s[idx] == s[idx+1]:
            erase_list.append(idx+1)

    erase_list.reverse()
    for idx in erase_list:
        s = s[:idx] + s[idx+1:]
    
    print(s)

s = "aaaaabbcc"
erase(s)