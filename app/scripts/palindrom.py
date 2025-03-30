string = "fdsaghdshfvdabcdefedcba"
j=1

for i in range(len(string)-1):
    if string[i] == string[i+1]:
        length = 2
        try:
            while j:
                if string[i-j] == string [i+j+1]:
                    length += 2
                    j += 1
                else:
                    break            
        except:
            print(string[int(i-length/2+1):int(i+length/2+1)])
            continue

    if string[i-1] == string[i+1]:
        try:
            length = 3
            while j:
                if string[i-j-1] == string [i+j+1]:
                    length += 2
                    j += 1
                else:
                    break
        except:
            print(string[int(i-length/2+1):int(i+length/2+1)])
            continue
