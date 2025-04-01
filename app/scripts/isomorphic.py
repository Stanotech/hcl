def are_isomorphic(str1, str2):
    
    def gather(str):
        dict = {}
        full_list= []
        for idx, char in enumerate(str):
            if char in dict:
                dict[char].append(idx)
            else:
                dict[char] = [idx]
        
        for sub_list in dict.values():
            full_list.append(sub_list)
        return full_list
    
    if gather(str1) == gather(str2):
        return True
    else:
        return False



print(are_isomorphic("egg", "add"))  # True
print(are_isomorphic("foo", "bar"))  # False
print(are_isomorphic("paper", "title"))  # True

