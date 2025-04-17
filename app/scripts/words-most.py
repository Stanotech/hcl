def second_most_frequent(words):
    counts = {}
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    sorted_dic = dict(sorted(counts.items(), key=lambda item:item[1]))

    return list(sorted_dic.keys())[-2]


words = [
    "apple", "banana", "apple", "orange", "banana", "banana",
    "apple", "grape", "grape", "grape", "grape"
]

print(second_most_frequent(words))  # "banana"