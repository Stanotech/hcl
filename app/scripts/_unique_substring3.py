# HCl. Write a Python function that finds the longest substring without repeating characters from a given string.

s = "abcghjabcvfdertyujhasd"
dic = {}
index_list = []
actual_indexes = []
longest_indexes = []

for idx, char in enumerate(s):
    if char in dic:
        dic[char].append(idx)
    else:
        dic[char] = [idx]

for key, value in dic.items():
    if len(value) == 1:
        index_list.append(value[0])

print(index_list)


for i in range(len(index_list)):
    if i < len(index_list) - 1:
        if index_list[i+1] -1 == index_list[i]:
            actual_indexes.append(index_list[i])
            print(actual_indexes)
        else:
            if len(actual_indexes) > len(longest_indexes):
                longest_indexes = actual_indexes
                actual_indexes = []


print(longest_indexes)
print(s[longest_indexes[0]:longest_indexes[-1]+2])





