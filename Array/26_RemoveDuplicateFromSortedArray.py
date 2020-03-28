def move_forward(start, counter, nums):
    if counter == 0:
        return nums
    index = start + counter + 1 
    for i in range(index, len(nums)):
        nums[i - index + 1 + start] = nums[i]
    return nums[:len(nums)-counter]


def RemoveDuplicate(nums):
    res = nums
    max_iter = max(nums) - min(nums)
    start_index = 0
    start = 0
    for _ in range(max_iter):
        res = move_forward(start, GetCounter(start_index, res), res)
        start_index += 1
        start += 1
    return res


def GetCounter(start_index, nums):
    counter = 0
    for i in range(start_index, len(nums)):
        for j in range(i+1, len(nums)):
            if nums[j] == nums[i]:
                counter += 1
            else:
                return counter
    return counter



nums = [0,0,1,1,2,2,3,3,3,3,3,3,4,5,5,5,5,6,6,6]
print(RemoveDuplicate(nums))