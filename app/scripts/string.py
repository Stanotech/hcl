# Longest string with unique chars

string = "gdowvdfnsadsoapdguregsadklpeierbyusaklhfhewkfnksmacnvjxcvxqlnfejrk"
string_now = string_max = ""
i=0

for i in range(len(string)):
    print(f"i={i}")
    for j in range(i, len(string)):
        print(f"j={j}")
        print(f"string_now= {string_now}")
        if string[j] not in string_now:
            string_now += string[j]
        else:
            if len(string_now) > len(string_max):
                string_max = string_now
            string_now = ""
            break
    print(f"string_max= {string_max} length= {len(string_max)}")