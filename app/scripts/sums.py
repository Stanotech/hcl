arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_arr = []
sum = max_sum = i = j = 0

for i in range(len(arr)):
    print(f"i={i}")
    for j in range(i, len(arr)):
        print(f"j={j}")
        sum += arr[j]
        print(f"sum{sum}")
        if sum > max_sum:
            print("purt")
            max_arr = arr[i:j+1]
            max_sum = sum
            print(f"maxarr{max_arr}")
            print(f"maxsum{max_sum}")
    sum=0
    print("\n")


print(max_sum)
print(max_arr)
