def top_n_words(string, num):
    cleaned_str=""
    dic = {}
    low_string = string.lower()
    for char in low_string:
        if char.isalpha() or char == " ":
            cleaned_str += char       

    words_list = cleaned_str.split(" ")
    for word in words_list:
        if word in dic:
            dic[word] += 1
        else:
            dic[word] = 1
    sorted_dic = sorted(dic.items(), key=lambda item:item[1])

    final_list = (sorted_dic[-num:])

    print([word for word, count in final_list])       
    


top_n_words("To be or not to be, that is the question.", 2)  
# ['be', 'to']

top_n_words("Hello world! Hello everyone. Welcome to the world of programming.", 3)  
# ['hello', 'world', 'to']

top_n_words("a a a b b c", 1)  
# ['a']