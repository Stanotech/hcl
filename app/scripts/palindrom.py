s = "fdsbaabghdshfvdabcdefedcba"
longest = ""

for i in range(len(s)):
    for even in (True, False):
        length = 2 if even else 1
        j = 0
        
        while True:
            left = i - j if even else i - j
            right = i + j + 1
            
            if left < 0 or right >= len(s) or s[left] != s[right]:
                break

            length += 2
            j += 1

        palindrome = s[left + 1:right]
        if len(palindrome) > len(longest):
            longest = palindrome

print("Najdłuższy palindrom:", longest)