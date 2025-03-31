# Sum all numbers excep those which occur more than once
nums = [5, 5, 5, 7, 9]
sum = 0

for i in range(len(nums)):
    if nums.count(nums[i]) > 1:
        continue
    else:
        sum += nums[i]

print(sum)