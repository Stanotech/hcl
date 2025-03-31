# Create list of multiplying all numbers except actual position

list = [1, 2, 6, 4, 2, 7, 5, 3]
end_list =[]
number = 1

for i in range(len(list)):
    multi_list = list.copy()
    del multi_list[i]
    for j in multi_list:
        number *= j
    end_list.append(number)
    number = 1

print(end_list)