def longest_palindrome(str):
    str2 = "#" + "#".join(str) + "#"
    longest = ""
    for idx in range(len(str2)+1):
        leng = 0
        while idx - leng >= 0 and idx + leng <= len(str2)-1 and str2[idx - leng] == str2[idx + leng]:              
            actual = str2[idx-leng:idx+leng+1]
            if len(actual) > len(longest):
                longest = actual
            leng += 1

    longest = longest.replace("#", "")
    print(longest)
    return longest

assert longest_palindrome("racecar") == "racecar"
assert longest_palindrome("banana") == "anana"
assert longest_palindrome("abcde") == "a"

