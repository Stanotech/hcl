def find_balanced_substring(s):
    longest = ""
    num_count = 0
    letter_count = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            if s[j].isdigit():
                num_count += 1
            elif s[j].isalpha():
                letter_count += 1
            
            if num_count == letter_count and len(s[i:j+1]) > len(longest):
                longest = s[i:j+1]
        num_count = 0
        letter_count = 0
    
    print(longest)
    return longest


assert find_balanced_substring("abc123") == "abc123"
assert find_balanced_substring("a1b2c3dxyz") == "a1b2c3"
assert find_balanced_substring("abcxyz") == ""