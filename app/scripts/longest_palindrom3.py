def longest_palindrome(str):
    str = "#" + "#".join(str) + "#"
    longest = ""
    for idx in range(len(str)-1):
        leng = 0
        while idx - leng >= 0 and idx + leng <= len(str)-1 and str[idx - leng] == str[idx + leng]:
            actual = str[idx - leng : idx + leng + 1]
            if len(actual) > len(longest):
                longest = actual
            leng += 1

    longest = longest.replace("#", "")
    print(longest)
    return longest

assert longest_palindrome("racecar") == "racecar"
assert longest_palindrome("banana") == "anana"
assert longest_palindrome("abcde") == "a"

