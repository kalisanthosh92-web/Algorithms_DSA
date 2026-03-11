nums = [3,1,3,2]

duplicates = 0
n = len(nums)

for i in range(n):
    min_i = i
    for j in range(i+1,n):
        if nums[j] < nums[min_i]:
            min_i = j

    if nums[i] == nums[min_i] and min_i != i :
        duplicates += 1

    nums[i], nums[min_i] = nums[min_i], nums[i]
print(duplicates)

