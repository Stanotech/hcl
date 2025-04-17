# HCl. Write a Python function that finds the longest substring without repeating characters from a given string.

s = "abcghjabcvfdertyujhasd"
dic = {}
for idx, char in enumerate(s):
    if char not in dic:
        dic[char] = []
    dic[char].append(idx)

index_list = []
for char, indexes in dic.items():
    if len(indexes) > 1:
        index_list.extend(indexes)

sorted_list= sorted(index_list)

longest = ""
for index in range(len(sorted_list)-1):
    leng = sorted_list[index+1] - sorted_list[index]
    if leng > 1 and leng > len(longest):
        longest = s[sorted_list[index]:sorted_list[index+1]]


print(longest)






