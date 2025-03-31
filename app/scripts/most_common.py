# Most common digit in lists

nums = [1, 3, 2, 3, 4, 1, 3, 2, 1, 1, 5, 5, 5, 5, 5]
dic = {}
most = 0
most_digit = ""

for i in range(len(nums)):
    if nums[i] not in dic:
        dic[nums[i]] = 1
    else:
        dic[nums[i]] += 1
        if dic[nums[i]] > most:
            most = dic[nums[i]]
            most_digit = str(nums[i])

print(f"Most common digit is {most_digit} it appears {most} times")

