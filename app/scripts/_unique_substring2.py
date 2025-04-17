# HCl. Write a Python function that finds the longest substring without repeating characters from a given string.

s = "abcghjabcvfdertyujhasd"
actual = ""
longest = "" 

for i in range(len(s)):
    for j in range(i, len(s)):
        if s[j] in actual:
            if len(actual) > len(longest):
                longest = actual
            actual = ""
            break
        else:
            actual += s[j]
    print (actual)
    print (longest)
    





