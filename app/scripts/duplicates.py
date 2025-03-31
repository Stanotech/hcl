# Erase duplicates

arr = [1, 1, 1, 2, 2, 2, 3, 4, 4, 5, 6, 6, 7, 7]
i = 0

while i < len(arr)-1:
    if arr[i] == arr[i+1]:
        arr.pop(i)
        continue
    i += 1

print(len(arr))
print(arr)