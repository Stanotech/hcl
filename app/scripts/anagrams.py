# Print out all anagrams from string

s = "cbaebabacdacbca"
target = "abc"

for i in range(len(s)):
    anagram = s[i:i+len(target)]
    for char in target:  
        idx = anagram.find(char)
        if idx != -1:
            anagram = anagram[:idx]+ anagram[idx+1:]
            if len(anagram) == 0 and len(s[i:i+len(target)]) == 3:
                print(s[i:i+len(target)])
        else:
            break

            
