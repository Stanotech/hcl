# Write a Python function that finds the longest substring without repeating characters from a given string.

s = "abcghjabcvfdertyujhasd"

s_max = ""
indexes = []
dic = {}
max_length = 0

for idx, char in enumerate(s):
    if char in dic:
        dic[char].append(idx)
    else:
        dic[char] = [idx]

for key in dic:
    if len(dic[key]) > 1:
        for id in dic[key]:
            indexes.append(id)

indexes.sort()

for idx in range(len(indexes)-1):
    length = indexes[idx+1] - indexes[idx]
    if length > max_length:
        max_length = length
        s_max = s[indexes[idx]:indexes[idx+1]]

print(s_max)




