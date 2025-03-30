string = "fdsaghdshfvdabcdefedcba"

for i in range(len(s) - 1):
        for even in (True, False):  # Sprawdzamy zarówno parzyste, jak i nieparzyste palindromy
            length = 2 if even else 3
            j = 1
            try:
                while True:
                    left = i - j if even else i - j - 1
                    right = i + j + 1
                    if s[left] == s[right]:
                        length += 2
                        j += 1
                    else:
                        break
            except IndexError:
                print(s[int(i - length / 2 + 1):int(i + length / 2 + 1)])
                continue
