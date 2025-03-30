nums = [-10, -5, 0, 3, 4, 5, 7, 9, 10, 15]
target = 10

idx1= 0
idx2= len(nums)-1

while idx1 < idx2:

    if nums[idx1] + nums[idx2] == target:
        print(f"pair of numbers: {nums[idx1]} & {nums[idx2]}")
        idx2 -= 1
        idx1 -= 1

    if nums[idx1] + nums[idx2] < target:
        idx1 += 1

    if nums[idx1] + nums[idx2] > target:
        idx2 -= 1