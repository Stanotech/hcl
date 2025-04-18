def longest_palindrome(str):
    str2=""
    for char in str:
        str2 += f"#{char}"
    print(str2)
    longest = ""
    for idx, char in enumerate(str2):
        for leng in range(idx+1):
            if idx - leng >= 0 and idx + leng <= len(str2)-1:
                if str2[idx-leng] == str2[idx+leng]:
                    actual = str2[idx-leng:idx+leng+1]
                    if len(actual) > len(longest):
                        longest = actual
                    continue
                else:                    
                    break        
    
    longest = longest.replace("#", "")
    print(longest)
    return longest

assert longest_palindrome("racecar") == "racecar"
assert longest_palindrome("banana") == "anana"
assert longest_palindrome("abcde") == "a"