
def are_anagrams(str1, str2):
    def sort(str):
        dic = {}
        for char in str:
            if char in dic:
                dic[char] += 1
            else:
                dic[char] = 1

        return dic

    if sort(str1) == sort(str2):
        return True
    else:
        return False



print(are_anagrams("listen", "silent"))  # True
print(are_anagrams("triangle", "integral"))  # True
print(are_anagrams("apple", "pale"))  # False