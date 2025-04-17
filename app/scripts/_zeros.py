# HCl first script. Zeros to end.


arr = [0, 0, 0, 1, 0, 4, 3, 0, 4, 9, 10, 0, 0, 0]
j = 0

n= len(arr)

#for i in range(len(arr)):
#    if arr[i] != 0:
#        arr[j], arr[i] = arr[i], arr[j]
#        j += 1

for i in range(len(arr)):
    if arr[i] != 0:
        arr.insert(j, arr.pop(i))
        j += 1

print(arr)