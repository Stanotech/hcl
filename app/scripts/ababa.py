
# longest substring pair

first = ""
second = ""
next = ""
length = 0
max = 0
max_string = ""
s = "aabbabababbbbabababaa"

for idx in range(1, len(s)):
    print(f"idx {idx}, actual {s[idx]}, second {second}, next {next}, length {length}")

    if s[idx] != s[idx-1]:
        if s[idx] == next:                
            next = s[idx-1]
            length += 1
        else:
            if length > max:
                max = length
                max_string = s[idx-length:idx]
            second = s[idx]
            next = s[idx-1]
            length = 2
    

print(max_string)

    
    

