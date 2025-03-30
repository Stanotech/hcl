nums = [-20, -15, -10, -5, 0, 2, 3, 6, 7, 8, 9, 12, 14, 16, 18, 21, 23]
target = 18

idx1= 0
idx2= len(nums)-1

while idx1 < idx2:

    if nums[idx1] + nums[idx2] == target:
        print(f"pair of numbers: {nums[idx1]} & {nums[idx2]}")
        idx2 -= 1

    elif nums[idx1] + nums[idx2] < target:
        idx1 += 1

    elif nums[idx1] + nums[idx2] > target:
        idx2 -= 1