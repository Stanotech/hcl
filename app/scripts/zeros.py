# HCl first script. Zeros to end.


arr = [0, 0, 0, 1, 0, 4, 3, 0, 4, 9, 10, 0, 0, 0]
j = 0

n= len(arr)

for i in range(n):
    if arr[i] != 0:
        arr[i], arr[j] = arr[j], arr[i]
        j += 1


print(arr)