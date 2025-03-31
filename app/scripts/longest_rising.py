nums = []

if len(nums) == 0:
    print("Nums must have some elements")
else:
    longest = [nums[0]]
    j=0
    for i in range(1, len(nums)):
        if nums[i] < longest[j]:
            longest[j] = nums[i]        
        else:
            longest.append(nums[i])
            j += 1
    
    print(longest)
