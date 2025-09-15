def remove_duplicates(nums):
    i = 0
    for j in range(len(nums)):
        if j == 0 or nums[j] != nums[j-1]:
            nums[i] = nums[j]
            i += 1
    return i
