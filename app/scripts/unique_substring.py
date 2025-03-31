# Write a Python function that finds the longest substring without repeating characters from a given string.

s = "abcghjabcvfdertyujhasd"

s_max = ""
repeated_indexes = []
char_positions = {}
max_length = 0

for idx, char in enumerate(s):
    if char in char_positions:
        char_positions[char].append(idx)
    else:
        char_positions[char] = [idx]

for indexes in char_positions.values():
        if len(indexes) > 1:
            repeated_indexes.extend(indexes)

repeated_indexes.sort() # List of indexes of repeated characters

for idx in range(len(repeated_indexes)-1):
    length = repeated_indexes[idx+1] - repeated_indexes[idx]
    if length > max_length:
        max_length = length
        s_max = s[repeated_indexes[idx]+1:repeated_indexes[idx+1]]


print(s_max)




